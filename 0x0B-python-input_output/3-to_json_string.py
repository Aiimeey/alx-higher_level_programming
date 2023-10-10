#!/usr/bin/python3
"""JSON String Serializer Module"""
import json


def to_json_string(my_obj):
    """ Serialize an object to a JSON-formatted string"""
    data = json.dumps(my_obj)
    return data
