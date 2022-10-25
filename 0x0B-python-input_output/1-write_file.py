#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8)

    Args:
        filename: file we are writing to
        text: text to write to the file

    Return: Number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
        size = file.tell()
        
    return (size)
