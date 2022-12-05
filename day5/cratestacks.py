#!/usr/bin/env python

import re
from copy import deepcopy

parsephase = 0

stacks = {}
stacks2 = {}

def printstacks(stacks):
    for x in range(1, len(stacks)+1):
        print(f'{x}: ', end='')
        print(''.join(stacks[x]))

with open('input', 'r') as _in:
    for line in _in:
        line = line.rstrip()
        match parsephase:
            case 0:
                if len(line) >= 2 and line[1] == '1':
                    parsephase = 1
                    stacks2 = deepcopy(stacks)
                    continue
                for i in range(1, len(line), 4):
                    stack = i//4 + 1
                    if 'A' <= line[i] <= 'Z':
                        if stack not in stacks:
                            stacks[stack] = []
                        stacks[stack].insert(0, line[i])
            case 1:
                if len(line) == 0:
                    continue
                match = re.match('move (\d+) from (\d+) to (\d+)', line)
                crates, source, dest = int(match[1]), int(match[2]), int(match[3])
                print(f'moving {crates} from {source} to {dest}')
                for i in range(crates):
                    stacks[dest].append(stacks[source].pop())
                for i in range(-crates, 0):
                    stacks2[dest].append(stacks2[source].pop(i))

printstacks(stacks)
for i in range(1, len(stacks)+1):
    print(stacks[i][-1], end='')
print()

for i in range(1, len(stacks2)+1):
    print(stacks2[i][-1], end='')
print()
