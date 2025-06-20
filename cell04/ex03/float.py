#!/usr/bin/env python3

x = input("Give me a number: ")

x = float(x)
if int(x) == x:
    print("This number is an integer.")
else:
    print("This number is a decimal.")