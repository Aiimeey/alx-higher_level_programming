#!/usr/bin/python3
""" peak finder module """


def find_peak(list_of_integers):
    """
    function that finds a peak using binary search algorithm
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        md = (left + right) // 2

        if list_of_integers[md] < list_of_integers[md + 1]:
            left = md + 1
        else:
            right = md

    return list_of_integers[left]
