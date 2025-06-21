#!/usr/bin/env python3

a = [2, 8, 9, 48, 8, 22, -12, 2]

x = []
for i in a:
    if i > 5:
        x.append(i)
# for i in range(len(a)):
#     if a[i] > 5:
#         x.append(a[i] + 2)

print("Original array:", a)
print("New array:", x)
