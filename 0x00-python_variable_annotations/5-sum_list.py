#!/usr/bin/env python3
""" Defines a type annotated function that returns the sum of the
   values in the input list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of values in the input list """
    result: float = 0
    for num in input_list:
        result += num
    return result
