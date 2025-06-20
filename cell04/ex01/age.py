#!/usr/bin/env python3

i = int(input("Please tell me your age: "))
print(f"You are currently {i} years old")

i += 10
for x in range(1, 4):
    print(f"In {x * 10} years, you'll be {i} years old.")
    i += 10