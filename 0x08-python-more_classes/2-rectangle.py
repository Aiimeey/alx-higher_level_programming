#!/usr/bin/python3
"""A module defining a Rectangle class"""


class Rectangle:
    """ A class for creating and manipulating rectangle objects """

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle object with a given width and height
        Args:
            width (int): The width of the rectangle. Defaults to 0
            height (int): The height of the rectangle. Defaults to 0
        Raises:
            TypeError: If width or height are not integers
            ValueError: If width or height are less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle
        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle
        Args:
            value (int): The new width of the rectangle
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of the rectangle
        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle
        Args:
            value (int): The new height of the rectangle
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate and return the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate and return the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 | self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
