#!/usr/bin/python3
"""
 A module defining operation
"""


def matrix_divided(matrix, div):
    """ Divide each element in a matrix by a specified divisor

    Args:
        matrix (list of lists): The matrix to b divided must b integer or float
        div (int or float): The divisor by which each element is divided
    """
    if not all(
        isinstance(row, list) and
        all(isinstance(element, (int, float)) for element in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")

    if not all(
        len(row) == len(matrix[0])
        for row in matrix
    ):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return result_matrix
