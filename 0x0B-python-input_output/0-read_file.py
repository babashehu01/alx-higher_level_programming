#!/usr/bin/python3
"""
This module defines a file reading unction
"""


def read_file(filename=""):
    """
    This function writes/prints the contents of a file to stdout

    Args:
        filename: The file to be printed
    """
    with open(filename, encoding="utf-8") as file:
        output = file.read()

    print(output, end="")
