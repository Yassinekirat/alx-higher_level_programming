#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            uppercase_result = chr(ord(char) - 32)
        else:
            uppercase_result = char
        print("{}".format(uppercase_result), end="")
    print()
