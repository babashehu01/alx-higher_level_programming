#!/usr/bin/python3
'''Represents a class Rectangle'''


class Rectangle:
    '''Defines a Rectangle'''

    def __init__(self, width=0, height=0):
        '''initializes a new Rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''returns the value of Width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the value of Width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must >= 0')
        self.__width = value

    @property
    def height(self):
        '''returns the value of Height'''
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
        '''return the area of the Rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''return the perimeter of the Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = (2 * (self.__width + self.__height))
        return perimeter

    def __str__(self):
        '''string representation of Rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ''
        strpr = ''
        for i in range(self.__height):
            strpr += ('#' * self.__width)
            if i != self.__height - 1:
                strpr += '\n'
        return strpr

    def __repr__(self):
        '''class representantion of Rectangle'''
        return ('Rectangle({}, {})'.format(self.__width, self.__height))
