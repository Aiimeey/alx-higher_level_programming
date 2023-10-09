#!/usr/bin/python3
"""
A module containing a function for checking if an object is exactly an instance
"""


def is_same_class(obj, a_class):
    """ Check if the object is exactly an instance of the specified class

    Args:
    obj: The object to be checked.
    a_class: The class to check against
    """
    return type(obj) is a_class
