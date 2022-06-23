#!/usr/bin/env python3
""" Module defines a type annotated function """


def concat(str1: str, str2: str) -> str:
    """ Returns a concatenated string

    Args:
        str1 (string): First dtring
        str2 (string): Second string
    """
    return str1 + str2
