let rec sumElves (itemcalories:string list, sum:int) =
    match itemcalories with
    | [] -> [sum]
    | h::t ->
        if h = "" then
            sum::(sumElves (t, 0))
        else
            sumElves(t, sum +  (h |> int))
    
let inputFile = "../input"

let elves = sumElves (System.IO.File.ReadLines inputFile |> List.ofSeq, 0)

printfn $"{List.max elves}"
printfn $"{List.sum ((List.sortDescending elves)[0..2])}"
