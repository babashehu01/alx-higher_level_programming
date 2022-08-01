#!/usr/bin/python3
class Square:
    """
    Class for printing a square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        for i in range(0, self.__size):
            print("#"*self.__size)
        if self.__size == 0:
            print()
