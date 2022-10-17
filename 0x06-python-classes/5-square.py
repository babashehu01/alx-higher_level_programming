#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a new Square
        Args:
            size (int): size of the Square
        """
        self.size = size

    @property
    def size(self):
        """retrieves the size of the Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the area of the Square"""
        return (slef.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
