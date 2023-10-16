#!/usr/bin/python3
""" This module defines the Base class for managing unique identifiers """
import json
import os


class Base:
    """ Base class for managing unique identifiers"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a new instance of the Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves a list of objects to a JSON file """
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
        """ Converts a JSON string to a list of dictionaries """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of the cls & initializes it with a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Loads instances of the class from a JSON file """
        file_name = cls.__name__ + ".json"
        instances = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = file.read()
                if data:
                    js_list = cls.from_json_string(data)
                    for itm in js_list:
                        instance = cls.create(**itm)
                        instances.append(instance)
            return instances
        except FileNotFoundError:
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes a list of objects to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    data = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(data)
