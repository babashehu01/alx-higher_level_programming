#!/usr/bin/python3
''' Defines a class Square '''

from models.rectangle import Rectangle
import json


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        ''' Insatntiates a new Square '''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        ''' String representation of Square '''
        return "[Square] ({}) {}/{} - {}".format(

                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        ''' Returns the size '''
        return self.__width

    @size.setter
    def size(self, value):
        ''' sets the size '''
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        ''' Assigns Update the class Square by adding the attributes'''
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        ''' returns dictionary representation of Square '''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
