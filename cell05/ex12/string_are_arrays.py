#!/usr/bin/env python3

import  sys
import  re

x = 0

if len(sys.argv) != 2:
    print("none")
else:
    for i in range(len(sys.argv[1])):
        if sys.argv[1][i] == 'z':
            x += 1
    if x > 0:
        for i in range(x):
            print("z", end="")
    else:
        print("none", end="")
    print()