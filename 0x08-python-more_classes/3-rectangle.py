#!/usr/bin/python3
'''Represents a Rectangle'''


class Rectangle:
    '''Defines a Resctangle'''

    def __init__(self, width=0, height=0):
        '''initializes a new Rectangle'''
        self.width = width
        self.height = height

    def __repr__(self):
        '''representation of the class Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.__height):
            print('w')
            return ('#' * self.__width)

    @property
    def width(self):
        '''returns the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the value of width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be <= 0')
        self.__width = value

    @property
    def height(self):
        '''returns the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the height of the Rectangle'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('heght must be <= 0')
        self.__height = value

    def area(self):
        '''returns the area of the rectangke'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''return the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeter = (2 * (self.__height + self.__width))
            return perimeter
