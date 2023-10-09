#!/usr/bin/python3
""" module provides a function to retrieve available attributes and methods """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object

    """
    return list(dir(obj))
