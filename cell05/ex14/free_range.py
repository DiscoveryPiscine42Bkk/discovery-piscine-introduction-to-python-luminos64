#!/usr/bin/env python3

import  sys

if len(sys.argv) != 3:
    print("none")
elif not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    print("Please enter valid integers.")
else:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    ar = []
    if y < x:
        x, y = y, x
    for i in range(x, y + 1):
        ar.append(i)
    print(ar)