#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of a new Square
        Args:
            size (int): size of the Square
            position (tuple): position of the new Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the value of the Size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value to size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Return the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value of the positions"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the Square using #"""
        if self.__size == 0:
            print('')
        else:
            for i in range(0, self.__size):
                print(' ' * self.__position[0], '#' * self.__size)
