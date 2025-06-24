#!/usr/bin/env python3

import  sys
import  re

if len(sys.argv) < 2:
    print("none")
else:
    params = sys.argv[1:]
    for x in params:
        if not re.search(r"ism$", x):
            print(x + "ism")