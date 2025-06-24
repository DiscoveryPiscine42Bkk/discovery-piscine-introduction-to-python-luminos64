#!/usr/bin/env python3

import	sys

x = len(sys.argv)

if x != 3:
	print("none")
else:
	for i in reversed(range(len(sys.argv))):
		if sys.argv[i] and i > 0:
			print(sys.argv[i])
