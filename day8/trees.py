#!/usr/bin/env python

forest = []

with open('input', 'r') as _in:
    for line in _in:
        line = line.strip()
        forest.append(line)

visible = set()

for row in range(len(forest)):
    maxheight = -1
    for col in range(len(forest[row])):
        height = int(forest[row][col])
        if height > maxheight:
            maxheight = height
            visible.add((row,col))
    maxheight = -1
    for col in range(len(forest[row])-1, -1, -1):
        height = int(forest[row][col])
        if height > maxheight:
            maxheight = height
            visible.add((row,col))

for col in range(len(forest[0])):
    maxheight = -1
    for row in range(len(forest)):
        height = int(forest[row][col])
        if height > maxheight:
            maxheight = height
            visible.add((row,col))
    maxheight = -1
    for row in range(len(forest)-1, -1, -1):
        height = int(forest[row][col])
        if height > maxheight:
            maxheight = height
            visible.add((row,col))

print(len(visible))

def scenic(col, row):
    x, y = col, row
    trees_up = 0
    while y > 0:
        y -= 1
        trees_up += 1
        if forest[y][x] >= forest[row][col]:
            break

    y = row
    trees_down = 0
    while y < len(forest) - 1:
        y += 1
        trees_down += 1
        if forest[y][x] >= forest[row][col]:
            break

    y = row
    trees_left = 0
    while x > 0:
        x -= 1
        trees_left += 1
        if forest[y][x] >= forest[row][col]:
            break

    x = col
    trees_right = 0
    while x < len(forest[row]) - 1:
        x += 1
        trees_right += 1
        if forest[y][x] >= forest[row][col]:
            break
    
    return trees_up * trees_down * trees_left * trees_right

max_scenic = 0

for x in range(len(forest)):
    for y in range(len(forest[x])):
        s = scenic(x, y)
        if s > max_scenic:
            max_scenic = s

print(max_scenic)
