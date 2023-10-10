#!/usr/bin/python3
""" file writer module """


def write_file(filename="", text=""):
    """prints into a file and returns the number of char written"""
    with open(filename, "w", encoding="utf-8") as file:
        char_num = file.write(text)
        return char_num
