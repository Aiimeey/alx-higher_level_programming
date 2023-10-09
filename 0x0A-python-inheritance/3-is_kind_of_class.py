#!/usr/bin/python3
"""
A module containing a function for checking if an object is an instance
"""


def is_kind_of_class(obj, a_class):
    """ Check if the object is an instance of the specified class

    Args:
    obj: The object to be checked.
    a_class: The class to check against
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
