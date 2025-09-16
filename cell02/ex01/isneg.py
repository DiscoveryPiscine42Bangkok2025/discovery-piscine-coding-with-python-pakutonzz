#!/usr/bin/env python3

def main():
    number = int(input("."))
    if number == 0:
        print("This number is both positive and negative.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("This number is positive.")

if __name__ == "__main__":
    main()
