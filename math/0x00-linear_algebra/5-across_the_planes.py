#!/usr/bin/env python3
"""A module that contains a function
"""


def add_matrices2D(mat1, mat2):
    """a function that adds two matrices element-wise

    Args:
        mat1 (array): a matrice
        mat2 (array): a matrice

    Returns:
        array | None: the sum of matrices
    """
    if len(mat1) == len(mat2):
        result = []
        for i in range(len(mat1)):
            if len(mat1[i]) == len(mat2[i]):
                result.append(list(map(lambda x, y: x + y, mat1[i], mat2[i])))
            else:
                return None
        return result
    return None
