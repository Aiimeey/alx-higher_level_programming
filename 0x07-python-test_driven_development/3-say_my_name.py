#!/usr/bin/python3
"""
A module defining a function for printing a name.
"""


def say_my_name(first_name, last_name=""):
    """ Print a formatted name based on the provided first name and last name.
    Args:
        first_name (str): The first name to be included in the formatted name
        last_name (str): The last name to be included in the formatted name
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        elif (last_name and not isinstance(last_name, str)):
            raise TypeError("last_name must be a string")

        if last_name:
            print("My name is {} {}".format(first_name, last_name))
        else:
            print("My name is {} ".format(first_name))
    except TypeError as e:
        raise e
