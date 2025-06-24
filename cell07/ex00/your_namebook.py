#!/usr/bin/env python3

def array_of_names(list):
    res = []
    for x, y in list.items():
        full = x.title() + " " + y.title()
        res.append(full)
    return res

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))