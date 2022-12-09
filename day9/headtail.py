#!/usr/bin/env python3

def addt(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def move(dir):
    if dir=='U': return (0,1)
    if dir=='D': return (0,-1)
    if dir=='L': return (-1,0)
    if dir=='R': return (1,0)

def tailpop(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return(0,0)

    # check for straight moves
    if head[0] < tail[0] - 1 and head[1] == tail[1]:
        return (-1,0)
    elif head[0] > tail[0] + 1 and head[1] == tail[1]:
        return (1,0)
    elif head[1] < tail[1] - 1 and head[0] == tail[0]:
        return (0, -1)
    elif head[1] > tail[1] + 1 and head[0] == tail[0]:
        return (0,1)

    dx = 0
    dy = 0
    # do a diagonal move towards head
    if head[0] > tail[0]:
        dx = 1
    else:
        dx = -1
    if head[1] > tail[1]:
        dy = 1
    else:
        dy = -1
    return(dx, dy)


head = (0,0)
tail = (0,0)
taillog = set()

with open('input') as _in:
    for line in _in:
        line = line.strip()
        dir, count = line.split()
        count = int(count)
        for i in range(count):
            head = addt(head, move(dir))
            tail = addt(tail, tailpop(head, tail))
            taillog.add(tail)

print(len(taillog))

knots = []
for i in range(10):
    knots.append((0,0))

taillog = set()

with open('input') as _in:
    for line in _in:
        line = line.strip()
        dir, count = line.split()
        count = int(count)
        for i in range(count):
            for knot in range(len(knots)):
                if knot == 0:
                    knots[knot] = addt(knots[knot], move(dir))
                else:
                    knots[knot] = addt(knots[knot], tailpop(knots[knot-1], knots[knot]))
            taillog.add(knots[-1])

print(len(taillog))
