#!/usr/bin/python3
"""A module defining a Rectangle class"""


class Rectangle:
    """A class for creating and manipulating rectangle objects"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object with a given width and height
        Args:
            width (int): The width of the rectangle, defaults to 0
            height (int): The height of the rectangle, defaults to 0
        Raises:
            TypeError: If width or height are not integers
            ValueError: If width or height are less than or equal to 0
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get the width of the rectangle
        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle
        Args:
            value (int): The new width of the rectangle
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle
        Args:
            value (int): The new height of the rectangle
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value