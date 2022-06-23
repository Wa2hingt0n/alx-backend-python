#!/usr/bin/env python3
""" Defines a type annotated function that returns the sum
   of a mixed list of integers and floats """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of values of a mixed list of integers and floats """
    result: float = 0
    for num in mxd_lst:
        result += num
    return result
