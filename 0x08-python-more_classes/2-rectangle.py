#!/usr/bin/python3
"""A module defining a Rectangle class"""


class Rectangle:
    """ A class for creating and manipulating rectangle objects """

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle object with a given width and height
        Args:
            width (int): The width of the rectangle. Defaults to 0
            height (int): The height of the rectangle. Defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Return: The width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle
        Args:
            value (int): The new width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Return: The height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle
        Args:
            value (int): The new height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns: The area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Return: The perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
