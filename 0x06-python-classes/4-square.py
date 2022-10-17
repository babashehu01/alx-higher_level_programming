#!/usr/bin/python3
"""Defines a class Square"""


def __init__(self, size=0):
    def __init__(self, size):
        """Initialize a new square
        Args:
            size (int): Size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Gets/returns the current size"""
        return (self.__size)

    @size.setter
    def size(self):
        """sets the value of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of our square"""
        return (self.__size ** 2)
