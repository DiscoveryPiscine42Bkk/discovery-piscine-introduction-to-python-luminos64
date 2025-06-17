#!/usr/bin/env python3

x = input()
if x.isnumeric() == True:
    y = int(x)
    if y < 0:
        print("This number is negative.")
    elif y > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")