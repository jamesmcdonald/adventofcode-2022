#!/usr/bin/env python3

import os

files = {}

with open("input", "r") as _in:
    path = ""
    for line in _in:
        line = line.strip()
        if line.startswith('$'):
            if line.startswith("$ cd"):
                name = line[5:]
                if name == "/":
                    path = ""
                elif name == "..":
                    path = os.path.dirname(path)
                else:
                    path = os.path.join(path, name)
            if line.startswith("$ ls"):
                mode = "dir"
        elif line.startswith("dir"):
            pass # nothing to do with dir entries
        elif '0' <= line[0] <= '9':
            size, name = line.split(' ')
            size = int(size)
            files[os.path.join(path, name)] = size

dirsizes = {}

for file in files:
    dir = file
    while dir != "":
        dir = os.path.dirname(dir)
        if dir not in dirsizes:
            dirsizes[dir] = 0
        dirsizes[dir] += files[file]

print(dirsizes)

filtered = {k:v for (k,v) in dirsizes.items() if v <= 100000}

print(sum(filtered.values()))

neededspace = 30000000 - (70000000 - dirsizes[''])

print(next(filter(lambda x: x >= neededspace, sorted(dirsizes.values()))))
