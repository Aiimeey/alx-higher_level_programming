#!/usr/bin/python3
"""
This module provides a function to retrieve available attributes and methods
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    return dir(obj)
