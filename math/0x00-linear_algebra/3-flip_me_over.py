#!/usr/bin/env python3
"""A module that contains a function
"""


def matrix_transpose(matrix):
    """A function that returns the transpose of a matrix

    Args:
        matrix (array): a matrix to be transposed

    Returns:
        matrix (array): a transposed matrix
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
