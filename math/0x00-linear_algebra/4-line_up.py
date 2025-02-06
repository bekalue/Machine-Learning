#!/usr/bin/env python3
"""A module that contains a function
"""


def add_arrays(arr1, arr2):
    """A function that adds two arrays element-wise

    Args:
        arr1 (array): an array
        arr2 (array): an array

    Results:
        array | None : added array or none
    """
    if len(arr1) == len(arr2):
        return list(map(lambda x, y: x + y, arr1, arr2))
    return None
