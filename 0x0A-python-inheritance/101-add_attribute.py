#!/usr/bin/python3
"""
This module defines a function and a class for adding attributes to objects
"""


def add_attribute(obj, attribute, value):
    if hasattr(obj, '__dict__'):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
