#!/usr/bin/python3
"""
Defining a class Square
"""


class Square:
    """
    Adding private instance attribut size
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    """
    Adding a public instance method area
    """
    def area(self):
        return (self.__size * self.__size)
