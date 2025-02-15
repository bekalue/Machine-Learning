#!/usr/bin/env python3
"""A module that contains a function
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication on two 2D matrices.
    
    Args:
        mat1 (array): The first 2D matrix (list of lists) containing ints/floats.
        mat2 (array): The second 2D matrix (list of lists) containing ints/floats.
    
    Returns:
        array: A new matrix that is the product of mat1 and mat2,
    or None if the matrices cannot be multiplied.
    """
    # Check if matrices can be multiplied
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize the resulting matrix with zeros
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
