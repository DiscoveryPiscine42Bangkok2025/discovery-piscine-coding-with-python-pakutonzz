#!/usr/bin/env python3

def main():
    password = 'password'
    if input("Enter the password: ") == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()