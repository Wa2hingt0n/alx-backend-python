#!/usr/bin/env python3
""" Defines a type-annotated function returns the floor of a float """
from math import floor as fl


def floor(n: float) -> int:
    """ Returns the floor of a float as an integer

    Args:
        n (float): The number to be returned as a floor
    """
    return fl(n)
