#!/usr/bin/python3
for x in range(0, 9):
    for y in range(0, 10):
        if x < y:
            if x != 8 or y != 9:
                print("{}{}".format(x, y), end=", ")
            elif x == 8 and y == 9:
                print("{}{}".format(x, y))
