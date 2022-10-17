#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Initialize a new square
    Args:
        size (int): size of the new square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
    """Return the current Square area"""
        return (self.__size * self.__size)
