#!/usr/bin/python3
""" module that provides functions for working with text files """


def write_file(filename="", text=""):
    """Appends a string to the end of a text file, returns num of char added"""
    with open(filename, "a", encoding="utf-8") as file:
        char_num = file.write(text)
        return char_num
