#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asc = ord(char)
        if 97 <= asc <= 122:
            asc = asc - 32
        print("{}".format(chr(asc)), end="")
    print("")
