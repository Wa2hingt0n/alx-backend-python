#!/usr/bin/env python3
""" Defines a type annotated function to_kv """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple with the first element the string k and
        and the second element the square v
    """
    ret: float = v ** 2
    return (k, ret)
