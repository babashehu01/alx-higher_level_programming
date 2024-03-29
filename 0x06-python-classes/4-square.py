#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
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
    def size(self, value):
        """sets the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of our square"""
        return (self.__size * self.__size)
