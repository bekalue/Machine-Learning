#!/usr/bin/env python3
"""A module that contains a function
"""


def np_slice(matrix, axis= {}):
    """Function that slices a matrix along a specific axis

    Args:
        matrix (array): a matrix to be sliced
        axis (int): an axis

    Returns:
        array: sliced matrix
    """
    if not axis:
        return matrix
    buffer_list = []
    for i in range(len(matrix.shape)):
        flag = 0
        for j, k in axis.items():
            if j == i:
                buffer_list.append(slice(*k))
                flag = 1
                break
        if flag == 0:
            buffer_list.append(slice(None, None, None))
    return matrix[tuple(buffer_list)]
