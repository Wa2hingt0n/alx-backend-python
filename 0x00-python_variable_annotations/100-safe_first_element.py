#!/usr/bin/env python3
""" Defines a duck-typed annotated function """
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first element in the sequence if present, else None """
    if lst:
        return lst[0]
    else:
        return None
