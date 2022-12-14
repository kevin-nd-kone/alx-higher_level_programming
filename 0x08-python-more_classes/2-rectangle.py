#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:

    """Rectangle class constructor"""

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError('width must be an integer')
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        self.__width = width

    """With property getter"""
    @property
    def width(self):
        return self.__width

    """Height property getter"""
    @property
    def height(self):
        return self.__height

    """With property setter"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Height property setter"""
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height)*2
