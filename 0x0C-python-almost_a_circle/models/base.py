#!/usr/bin/python3
""" Base class module """

import json


class Base:
    """ My Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Instantiates the new Base object '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' that returns the JSON string representation
        of list_dictionaries

        Args:
            list_dictionaries: is a list of dictionaries '''
        if list_dictionaries is None or list_dictionaries == '[]':
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation
        of list_objs to a file '''
        filename = cls.__name__ + '.json'
        lists = []
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                for obj in list_objs:
                    lists.append(obj.to_dictionary())
            dic = cls.to_json_string(lists)

            file.write(dic)
