#!/usr/bin/python3
'''This module defines a `Geometry class`'''


class BaseGeometry:
    '''Represents a Geometry'''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value'''
        if type(value) is not int:
            raise TypeError('the message {} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
