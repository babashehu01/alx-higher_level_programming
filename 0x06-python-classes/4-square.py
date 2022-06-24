#!/usr/bin/python3
"""
Defining a class Square
"""


class Square:
    """___Initializing size___"""
    def __init__(self, size=0):
        self.__size = size
    """Setting size"""
    @property
    def size(self):
        return self.__size
    """Getting size"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.value = __size
    """Public instance method"""
    def area(self):
        return (self.__size ** 2)
