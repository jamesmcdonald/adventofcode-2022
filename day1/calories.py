#!/usr/bin/env python

elves = []
elves.append([])

with open("input", "r") as input:
    for line in input:
        line = line.strip()
        if line == "":
            elves.append([])
        else:
            elves[-1].append(int(line))

print(max(sum(x) for x in elves))
print(sum(sorted(sum(x) for x in elves)[-3:]))
