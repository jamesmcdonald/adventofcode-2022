(ns cratestacks.core
  (:gen-class) 
  (:require clojure.java.io))

(defn load-crate
  "Take a crate definition in the form \"[x] \" and a stack position, and load the crate"
  [stacks cdef pos]
  stacks
  (let [crate (nth cdef 1)]
    (if (and (>= (int crate) (int \A)) (<= (int crate) (int \Z)))
      (do
        ;(println (str "Loading " crate " at " pos))
        (into stacks {pos (conj (get stacks pos) crate)}))
      stacks)))

(defn crates-parse
  [stacks line]
  (if (get stacks :crates-done)
    stacks
    (if (and (> (count line) 1) (= (get line 1) \1))
      (into stacks {:crates-done true})
      (loop [stacks stacks remaining-line line pos 0]
        (if (empty? remaining-line)
          stacks
          (recur (load-crate
            stacks (take 4 remaining-line) (inc pos))
                 (subs remaining-line (min 4 (count remaining-line)))
                 (inc pos)))))))

(defn move-parse
  [stacks line]
  (if-some [[all crates source dest]
      (re-matches #"move (\d+) from (\d+) to (\d+)" line)]
        (let [crates (new Integer crates) source (new Integer source) dest (new Integer dest)]
          ;(println (str "moving " crates " from " source " to " dest " stacks: " stacks))
          (loop [stacks stacks counter crates]
            (if (= counter 0)
              stacks
              (recur (into stacks
                {dest (cons (first (get stacks source))(get stacks dest))
                 source (rest (get stacks source))})
                     (dec counter)))))
        stacks))

(defn move-parse2
  [stacks line]
  (if-some [[all crates source dest]
            (re-matches #"move (\d+) from (\d+) to (\d+)" line)]
    (let [crates (new Integer crates) source (new Integer source) dest (new Integer dest)]
      ;(println (str "move2 " crates " from " source " to " dest " stacks: " stacks))
      (let [stacks (loop [stacks stacks counter crates]
        (if (= counter 0)
          stacks
          (recur (into stacks
                       {dest (cons (nth (get stacks source) (dec counter)) (get stacks dest))})
                 (dec counter))))]
        (into stacks {source (drop crates (get stacks source))})))
    stacks))

(defn parser
  [lines]
  (let [stacks (dissoc (reduce crates-parse {} lines) :crates-done)
        stacks (reduce (fn [s [k v]] (into s {k (reverse v)})) {} stacks)
        stacks1 (reduce move-parse stacks lines)
        stacks2 (reduce move-parse2 stacks lines)]
    (do
      (println (reduce (fn [out key] (str out (first (get stacks1 key)))) "" (sort (keys stacks1))))
      (println (reduce (fn [out key] (str out (first (get stacks2 key)))) "" (sort (keys stacks2)))))))

(defn parsefile
  "Parse a file, hopefully"
  [filename parser]
  (with-open [rdr (clojure.java.io/reader filename)]
    (parser (line-seq rdr))))

(defn -main
  [& args]
  (parsefile "../input" parser))
