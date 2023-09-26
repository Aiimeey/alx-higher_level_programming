#!/usr/bin/python3
""" Class square """


class Square:

    def __init__(self, size=0):
        """
        Initialize a Square object with a given size

        Args:
            size (int): The size of the square default to 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
