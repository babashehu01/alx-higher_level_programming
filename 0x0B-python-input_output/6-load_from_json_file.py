#!/usr/bin/python3
"""
Defines a function `load_from_json_file`
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename: JSON ile

    Return:
        Object notation
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
