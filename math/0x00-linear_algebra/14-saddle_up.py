#!/usr/bin/env python3
"""A module that contains a function
"""
import numpy as np


def np_matmul(mat1, mat2):
    """ a function that performs a matrix multiplication

    Args:
        mat1 (array): a matrix
        mat2 (array): a matrix

    Returns:
        array: a multiplied matrix
    """
    return np.matmul(mat1, mat2)
