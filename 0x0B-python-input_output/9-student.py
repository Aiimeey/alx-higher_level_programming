#!/usr/bin/python3
""" script defines a Python class that represents a student's information """


class Student():
    """Represents a student's information."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
