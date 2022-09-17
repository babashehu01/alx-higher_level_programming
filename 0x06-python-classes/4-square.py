#!/usr/bin/python3
"""
Defining a class Square
"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square
        """
        self.size = size

    @property
    def size(self):
        """Returns the value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the area"""
        return (self.__size * self.__size)
