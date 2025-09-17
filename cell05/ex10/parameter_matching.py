#!/usr/bin/env python3
import sys

n = len(sys.argv) - 1

if n == 1:
    s = input("What was the parameter ? ")
    print("Good Job!" if s == sys.argv[1] else "Nope, sorry...")
else:
    print("none")

