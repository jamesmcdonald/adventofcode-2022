(defn unique-run
  [signal length]
  (loop [remainder signal pos 0]
    (if (< (count remainder) length)
      0
      (if (= length (count (set (take length remainder))))
        (+ pos 4)
        (recur (rest remainder) (inc pos))))))

(defn parsefile
  "Get a line from a file and check if for signal and message"
  [filename]
  (with-open [rdr (clojure.java.io/reader filename)]
    (let [line (first (line-seq rdr))]
      (do
        (println (unique-run line 4))
        (println (unique-run line 14))))))

(parsefile "input")
