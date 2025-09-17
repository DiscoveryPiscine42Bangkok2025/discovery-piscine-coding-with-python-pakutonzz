#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1

if n > 0:
    for x in sys.argv[1:]:
        if not x.endswith('ism'):
            print(x+'ism')
else:
    print("none")