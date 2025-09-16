#!/usr/bin/env python3

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 * num2
    print(num1, "*", num2, "=", result)

    if result == 0:
        print("This result is both positive and negative.")
    elif result < 0:
        print("This result is negative.")
    else:
        print("This result is positive.")

if __name__ == "__main__":
    main()
