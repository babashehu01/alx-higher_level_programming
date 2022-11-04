#!/usr/bin/python3
''' Defines `Rectangle` class '''

from models.base import Base
import json


class Rectangle(Base):
    ''' Represents a rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Instantiates the new Rectangle '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' gets/returns the value of width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' sets the value of width '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        ''' gets/returns the value of height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' sets/asssigns the value of height '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' gets/returns the value of x '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' sets/assigns the value of x '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        ''' gets/returns the value of y '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' sets/assigns the value of y'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        ''' returns the area of the rectangle '''
        return (self.__width * self.__height)

    def display(self):
        ''' prints the Rectangle instance with the character # '''
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        ''' string representation of rectangle '''
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        ''' Update '''
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
