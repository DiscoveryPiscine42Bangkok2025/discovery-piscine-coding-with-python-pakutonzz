#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1

if n == 2:
    arr = [x for x in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]
    print(arr)
else:
    print("none")