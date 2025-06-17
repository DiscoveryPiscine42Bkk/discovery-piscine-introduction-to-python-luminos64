#!/usr/bin/env python3

x = input()
if x.isnumeric() == True:
    y = int(x)
    if y == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")