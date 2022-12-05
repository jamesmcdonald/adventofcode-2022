#!/usr/bin/env python

shapescore = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

outcomescore = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}

winscore = {
    'A X': 0+3,
    'A Y': 3+1,
    'A Z': 6+2,
    'B X': 0+1,
    'B Y': 3+2,
    'B Z': 6+3,
    'C X': 0+2,
    'C Y': 3+3,
    'C Z': 6+1,
}

score = 0
newscore = 0

with open('input', 'r') as _in:
    for line in _in:
        line = line.strip()
        score += outcomescore[line]
        score += shapescore[line[2]]
        newscore += winscore[line]
        print(line, outcomescore[line], shapescore[line[2]])

print(score)
print(newscore)
