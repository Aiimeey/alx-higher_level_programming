#!/usr/bin/python3
""" The function serializes the 'my_obj' parameter into a JSON format
    and writes it to the specified file"""
import json
import sys
from os import path


def save_to_json_file(my_obj, filename):
    """Serialize and save the given object to a JSON file"""
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)


def load_from_json_file(filename):
    """ Deserialize JSON data frm file and return the Python object"""
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)


filename = "add_item.json"
if not path.exists(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
