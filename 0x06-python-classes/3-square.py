#!/usr/bin/python3
"""
Nothing to import
"""


class Square:
    """
    Private instance attribute
    public instance method
    """
    def init(self,size=0):
        try:
            assert type(size) == int
        except:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")


    def area(self):
        """
        public instance method
        returns the current square area
        """
        return self.__size ** 2
