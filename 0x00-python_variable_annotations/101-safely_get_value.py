#!/usr/bin/env python3
""" Defines a function safely_get_value """
from typing import Mapping, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Safetly retrieves a key from a dictionary if it exists """
    if key in dct:
        return dct[key]
    else:
        return default
