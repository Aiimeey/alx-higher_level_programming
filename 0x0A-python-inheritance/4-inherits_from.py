#!/usr/bin/python3
"""
A module containing a function for checking if an object is
an instance of a class or its subclass
"""


def inherits_from(obj, a_class):
    """ Check if obj is an instance of a class or its subclass

    Args:
    - obj: The object to check for inheritance
    - a_class: The class to check for inheritance
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
