#!/usr/bin/python3
""" A module defining a Square class """


class Square:
    """A class for creating and manipulating square objects"""

    def __init__(self, size=0):
        """
        Initialize a Square object with a given size

        Args:
            size (int): The size of the square, defaults to 0
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """
        Get the size of the square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): The new size of the square
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
