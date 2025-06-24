#!/usr/bin/env python3

a = [2, 8, 9, 48, 8, 22, -12, 2]

x = []
for i in range(len(a)):
    if a[i] > 5:
        x.append(a[i] + 2)

y = set()

for i in x:
    if i > 5:
        y.add(i)

# for i in range(len(a)):
#     if a[i] > 5:
#         x.append(a[i] + 2)

print("Original array:", a)
print("New array:", y)
