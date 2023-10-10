#!/usr/bin/python3
"""A simple script that loads JSON data from a file """
import json


def load_from_json_file(filename):
    """ Deserialize JSON data frm file and return the Python object"""
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)
