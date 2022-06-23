#!/usr/bin/env python3
""" Defines a type annotated function that returns a function
    that multiplies a float by a multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    def product(num: float) -> float:
        """ Returns the product of a number and multiplier """
        return num * multiplier

    return product
