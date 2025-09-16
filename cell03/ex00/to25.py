#!/usr/bin/env python3

def main():
    num = int(input("Enter a number less than 25\n"))
    if num > 25 :
        print("Error")
    for i in range(num, 26):
        print("Inside the loop, my variable is ", i)

if __name__ == "__main__":
    main()