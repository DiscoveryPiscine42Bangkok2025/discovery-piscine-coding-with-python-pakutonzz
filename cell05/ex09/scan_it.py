#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1

if n == 2:
    key = sys.argv[1]
    s = sys.argv[2]
    count = s.count(key)
    print(count if count > 0 else "none")
else:
    print("none")



