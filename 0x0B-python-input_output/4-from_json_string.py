#!/usr/bin/python3
"""JSON String deserializer Module"""
import json


def from_json_string(my_str):
    """ deserialize an object to a python data structure"""
    data = json.loads(my_str)
    return data
