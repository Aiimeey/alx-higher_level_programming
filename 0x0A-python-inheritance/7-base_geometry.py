#!/usr/bin/python3
"""
This module provides a base class for geometric shapes and operations
"""


class BaseGeometry():
    """
    A base class for geometric shapes and operations
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate that a value is an integer greater than 0
        Args:
            name (str): The name of the variable being validated
            value: The value to be validated
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
