#!/usr/bin/python3
""" The function serializes the 'my_obj' parameter into a JSON format
    and writes it to the specified file"""
import json


def save_to_json_file(my_obj, filename):
    """Serialize and save the given object to a JSON file"""
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
