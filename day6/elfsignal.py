#!/usr/bin/env python

def unique_run(s, l):
        for i in range(len(line) - l):
            s = set(line[i:i+l])
            if len(s) == l:
                return i+l
        return None


with open('input', 'r') as _in:
    for line in _in:
        line = line.strip()
        print("signal after", unique_run(line, 4))        
        print("message after", unique_run(line, 14))
