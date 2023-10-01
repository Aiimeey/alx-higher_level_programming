#!/usr/bin/python3
""" A module defining a Square class """


class Square:
    """A class for creating and manipulating square objects"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a Square object with a given size and position

        Args:
            size (int): The size of the square defaults to 0
            position (tuple): The position of the square defaults to (0, 0)
        Raises:
            TypeError: If size or position are not of the correct types
            ValueError: If size or position have invalid values
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Get the size of the square

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square

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

    @property
    def position(self):
        """ Get the position of the square

        Returns:
            tuple: The position as a tuple of two positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position of the square

        Args:
            value (tuple): The new position of the square
        Raises:
            TypeError: If value is not a tuple or length != 2 or not integer
            ValueError: If any element in the tuple is less than 0
        """
        if type(value) is not tuple or len(value) != 2 or \
           not all(type(i) is int for i in value) or \
           any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculate and return the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Print the square using the character '#'

        If size is equal to 0, it prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
