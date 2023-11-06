#!/usr/bin/python3

"""
The function add_intege returns the sum of two integers
"""

def add_integer(a, b=98):
    """This adds the two integers function body"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
