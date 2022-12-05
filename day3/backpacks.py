#!/usr/bin/env python3

import re

def priority(letter):
    return ord(letter) - 96 if letter >= 'a' else ord(letter) - 38

total = 0
badges = 0

with open('input', 'r') as _in:
    i=0
    prev=""
    for line in _in:
        line = line.strip()
        s1 = line[0:len(line)//2]
        s2 = line[len(line)//2:]
        match = re.match(f'.*([{s1}]).*', s2)[1]
        total += priority(match)

        if i == 0:
            prev = line
        if i == 1:
            prev = set(line).intersection(prev)
        if i == 2:
            match = prev.intersection(line)
            badges += priority(list(match)[0])
        i = (i+1) % 3


print(total)
print(badges)
