#!/usr/bin/python3
""" custom list module that extends the functionality of built-in list class"""


class MyList(list):
    """ Custom list class that inherits from the built-in list class """

    def print_sorted(self):
        """ Print the elements of the list in ascending sorted order """
        print(sorted(self))
