#!/usr/bin/python3
"""
A module containing a function for checking if an object is an instance
"""


def inherits_from(obj, a_class):

    return issubclass(type(obj), a_class) and type(obj) is not a_class
