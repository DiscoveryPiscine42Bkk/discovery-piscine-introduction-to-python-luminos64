#!/usr/bin/env python3

def average(dic_l):
    i = 0
    avg = 0
    for x in dic_l.values():
        avg += x
        i += 1
    avg = avg / i
    return avg



class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")