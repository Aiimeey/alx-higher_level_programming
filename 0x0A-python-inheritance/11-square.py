#!/usr/bin/python3
"""
This module provides a base class for geometric shapes and operations
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class, a subclass of Rectangle for representing square shapes"""
    def __init__(self, size):
        """ Initializes a new Square instance """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Returns a string representation of the Square object """
        return "[Square] {}/{}".format(self.__size, self.__size)
