#!/usr/bin/env python3

try:
    x = int(input("Enter a number less than 25\n"))
except ValueError:
    print("Please enter valid integers.")
    exit()

if (x > 25):
    print("Error")
else:
    for x in range(x, 26):
        print("Inside the loop, my variable is", x)