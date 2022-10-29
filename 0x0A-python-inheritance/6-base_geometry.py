#!/usr/bin/python3
'''This module defines a `Geometry class`'''


class BaseGeometry:
    '''Represents a Geometry'''
    
    def area(self):
        raise Exception('area() is not implemented')
