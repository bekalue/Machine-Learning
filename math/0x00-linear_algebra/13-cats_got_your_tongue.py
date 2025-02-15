#!/usr/bin/env python3
"""A module that
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """a function that concatenates two matrices along the axis

    Args:
        mat1 (array): a matrix
        mat2 (array): a matrix
        axis (int): an axis

    Returns:
        array: concatenated array
    """
    return np.concatenate((mat1, mat2), axis)
