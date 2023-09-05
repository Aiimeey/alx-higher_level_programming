#!/usr/bin/python3
def remove_char_at(str, n):
    res =""
    ln = len(str)
    for x in range(ln):
        if x == n:
            continue
        res += str[x]
    return res