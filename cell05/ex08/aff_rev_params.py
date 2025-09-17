#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1
if n > 2 :
    for i in range(n, 0, -1):
        print(sys.argv[i])
else:
    print("none")
