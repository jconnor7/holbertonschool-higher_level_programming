#!/usr/bin/python3
"""Divide a matrix """


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.
    Args:
         Matrix: lists of integers or floats.
         Div: integer or float that the matrix is divided by.
    new_matrix:
        For every element in the row slice assign to replace col.
    Return:
         Divided elements of a matrix rounded to 2 decimal places.
    """

    if isinstance(matrix, list) is False \
            or any(isinstance(row, list) for row in matrix) is False:
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if all(isinstance(col, (int, float)) for row in matrix
           for col in row) is False:
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(len(row) == len(next(iter(matrix))) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for elem in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), elem)))
    return new_matrix
