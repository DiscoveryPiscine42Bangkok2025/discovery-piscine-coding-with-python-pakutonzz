#!/usr/bin/env python3

def main():
    i = 0
    while i < 11:
        line = f"Table de {i}:"
        j = 0
        while j < 11:
            line += f" {i * j}"
            j += 1
        print(line)
        i += 1

if __name__ == "__main__":
    main()