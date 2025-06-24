#!/usr/bin/env python3

import  sys

def shrink(line):
    print(line[:8])

def enlarge(line):
    line = str(line)
    while len(line) < 8:
        line += 'Z'
    print(line)

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        x = len(sys.argv[i])
        if x < 8:
            enlarge(sys.argv[i])
        else:
            shrink(sys.argv[i])