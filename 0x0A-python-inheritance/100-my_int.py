#!/usr/bin/python3
"""This module defines a custom integer class"""


class MyInt(int):
    """Custom integer class that inverts equality and inequality operators"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
