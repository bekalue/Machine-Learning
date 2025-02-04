#!/usr/bin/env python3
"""A module that contains a function.
"""


def matrix_shape(matrix):
    """A function that calculates the shape of a matix

    Args:
        matrix(array): a matrix

    Returns:
        array: the shape of a matrix
    """
    shape = [len(matrix)]
    while isinstance(matrix[0], list):
        shape.append(len(matrix[0]))
        matrix = matrix[0]
    return shape
