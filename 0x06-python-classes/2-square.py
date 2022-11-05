#!/usr/bin/python3
"""
Nothing to import
"""


class Squarre:
    """

    """
    def __init__(self, size=0):
        """
        """
        self.__size = size
        try:
            assert type(size) == int
        except TypeError:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
