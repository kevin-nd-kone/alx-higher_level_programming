#!/usr/bin/python3
"""
Nothing to import
"""


def add_integer(a, b=98):
    """
        add two integer
    """
    try:
        assert type(a) in (int, float)
    except TypeError:
        raise TypeError('a must be an integer')
    try:
        assert type(b) in (int, float)
    except TypeError:
        raise TypeError('b must be an integer')
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    return a + b
