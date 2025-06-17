#!/usr/bin/env python3

def main():
    try:
        x = int(input("Enter a number less than 25\n"))
    except ValueError:
        print("Please enter valid integers.")
        return
    if (x >= 25):
        print("Error")