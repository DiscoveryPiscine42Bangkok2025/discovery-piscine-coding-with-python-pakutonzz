#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1
print(sys.argv[1] if n > 0 else "none")