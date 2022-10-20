#!/usr/bin/python3
'''Defines a class Rectangle'''


class Rectangle:
    '''Defines a Rectangle'''

    def __init__(self, width=0, height=0):
        '''initializes a new rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''returns the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the value of width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''return the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the value of height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''returns the area of the Rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the perimeter of the Recctangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''repr representation of Rectangle'''
        strp = ''
        for i in range(self.__height):
            strp += ('#' * self.__width) + '\n'
        return strp
