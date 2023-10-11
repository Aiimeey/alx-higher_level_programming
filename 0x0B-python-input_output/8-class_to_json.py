#!/usr/bin/python3
"""defines a function that converts an object's attributes into a dictionary"""


def class_to_json(obj):
    """Convert object attributes to a filtered dictionary """
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result.update({key: value})
    return result
