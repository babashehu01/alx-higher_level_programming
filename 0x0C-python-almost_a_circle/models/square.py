#!/usr/bin/python3
''' Defines a class Square '''

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        ''' Insatntiates a new Square '''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        ''' String representation of Square '''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
