#!/usr/bin/python3
"""
 A module defining operation
"""


def add_integer(a, b=98):
    """ Adds two integers
    Args:
        a (int or float): The first integer or float to be added.
        b (int or float): second integer or float to be added. Default is 98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
