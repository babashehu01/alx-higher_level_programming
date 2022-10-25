#!/usr/bin/python3
"""
Defines a function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object represented by a JSON string
    """
    python_repr = json.loads(my_str)

    return (python_repr)
