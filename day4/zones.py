#!/usr/bin/env python3

contained = 0
overlaps = 0

with open('input', 'r') as _in:
    for line in _in:
        line = line.strip()
        elf1, elf2 = line.split(',')
        a, b = elf1.split('-')
        c, d = elf2.split('-')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if a <= c and b >= d or c <= a and d >= b:
            contained += 1
        if b >= c and a <= d:
            overlaps += 1

print(contained)
print(overlaps)
