#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1
print(sys.argv[1].lower() if n == 1 else "none")