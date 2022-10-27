#!/usr/bin/python3
"""
Defines a `save_to_json_file` function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be converted to json
        filename: file to be written to
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)
