#!/usr/bin/env python3
"""A module that contains a function
"""


def np_elementwise(mat1, mat2):
    """A function that does maths on matrices element-wisely

    Args:
        mat1 (list of list): a matrix
        mat2 (list of list): a matrix

    Returns:
        tuple: results of maths operations
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
