use std::io::{BufRead, BufReader};

fn main() {
    let mut elves = vec![];
    let infile = std::fs::File::open("../input").unwrap();
    let mut buf = String::new();
    let mut bufreader = BufReader::new(infile);
    let mut sum = 0;
    loop {
        buf.clear();
        let n = bufreader.read_line(&mut buf).expect("weird IO error");
        if n == 0 {
            break;
        }
        let line = buf.strip_suffix("\n").unwrap();
        match line {
            "" => {
                elves.push(sum);
                sum = 0;
            }
            x => sum += x.parse::<u32>().unwrap(),
        }
    }
    if sum > 0 {
        elves.push(sum)
    }

    println!("{}", elves.iter().max().unwrap());
    elves.sort_by(|a, b| b.partial_cmp(a).unwrap());
    println!("{}", elves.iter().take(3).sum::<u32>());
}
