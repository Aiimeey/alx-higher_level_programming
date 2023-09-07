#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_args = len(sys.argv) - 1

    args = sys.argv[1:]
    if len_args == 0:
        print("0 arguments.")

    elif len_args == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len_args))
        for i in range(1, len_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
