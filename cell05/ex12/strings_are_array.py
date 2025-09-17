#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1

if n == 1:
    count = sys.argv[1].count('z')
    print("z"*count if count > 0 else "none")
else:
    print("none")