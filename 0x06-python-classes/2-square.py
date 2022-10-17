#!/usr/bin/python3
"""Defines a class Square"""


class Sqaure:
    def __inti__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        self.__size = size
