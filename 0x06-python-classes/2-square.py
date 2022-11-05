#!/usr/bin/python3
"""
Nothing to import
"""


class Square:
    """
    define class body
    """
    def __init__(self, size=0):
        """
        class constructor definition
        """
        self.__size = size
        try:
            assert type(size) == int
        except:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
