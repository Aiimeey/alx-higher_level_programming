#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_args = len(sys.argv) - 1
    sum = 0

    for i in range(1, len_args + 1):
        sum += int(sys.argv[i])
    print("{}".format(sum))
