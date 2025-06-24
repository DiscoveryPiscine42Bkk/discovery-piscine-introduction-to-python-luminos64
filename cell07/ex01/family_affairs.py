#!/usr/bin/env python3

# def find_the_redheads(dic):
#     res = []
#     for x, y in dic.items():
#         if y == "red":
#             res.append(x)
#     return res

def find_the_redheads(dic_l):
    redheads = filter(lambda name: dic_l[name] == 'red', dic_l.keys())
    return list(redheads)


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))