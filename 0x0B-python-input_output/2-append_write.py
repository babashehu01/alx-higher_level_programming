#!/usr/bin/python3
"""
This module defines a function that appends a 
string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        size = file.tell()

    return (size)
