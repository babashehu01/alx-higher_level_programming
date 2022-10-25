#!/usr/bin/python3
"""
This module defines a function that returns the JSON
representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation
    of an object (string)

    Args:
        my_obj: Object/to be searialized

    Returns: JSON Representation o the obj
    """
    json_repr = json.dumps(my_obj)

    return json_repr
