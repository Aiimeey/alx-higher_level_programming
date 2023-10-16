#!/usr/bin/python3
""" This module defines the Base class for managing unique identifiers """
import json
import os


class Base:
    """ Base class for managing unique identifiers"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dict_list = []

        for obj in list_objs:
            if isinstance(obj, cls):
                dict_list.append(obj.to_dictionary())

        with open(filename, "w") as file:
            json_str = cls.to_json_string(dict_list)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        instances = []
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                js_str = file.read()
                dict_list = json.loads(js_str)
                instances = [cls.create(**dic) for dic in dict_list]
        return instances
