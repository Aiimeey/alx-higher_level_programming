#!/usr/bin/python3
""" module provides a function to retrieve attributes and methods """


def lookup(obj):
    """
    A function that returns the available
        attributes and methods of an object
    """
    return list(dir(obj))
