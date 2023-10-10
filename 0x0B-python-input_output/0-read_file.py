#!/usr/bin/python3
"""File Reader Module"""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
