#!/usr/bin/env python3
"""a module that contains a function
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis.
    
    Parameters:
    - mat1: The first 2D matrix (list of lists) containing ints/floats.
    - mat2: The second 2D matrix (list of lists) containing ints/floats.
    - axis: The axis along which to concatenate the matrices (default is 0).
    
    Returns:
    A new matrix that is the concatenation of mat1 and mat2 along the specified axis,
    or None if the matrices cannot be concatenated.
    """
    if axis == 0:
        # Check if the number of columns in both matrices are the same
        if all(len(row) == len(mat1[0]) for row in mat1) and all(len(row) == len(mat2[0]) for row in mat2):
            return mat1 + mat2
        else:
            return None
    elif axis == 1:
        # Check if the number of rows in both matrices are the same
        if len(mat1) == len(mat2):
            return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
        else:
            return None
    else:
        return None
