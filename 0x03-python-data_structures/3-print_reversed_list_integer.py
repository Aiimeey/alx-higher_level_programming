#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for x in reversed(my_list[0:len(my_list)]):
            print("{:d}".format(x))
