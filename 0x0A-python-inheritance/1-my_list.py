#!/usr/bin/python3
"""
Deines `MyList` class
"""


class MyList(list):
    """
    Represents a list
    """
    def print_sorted(self):
        """
        prints a list in sorted order
        """
        print(sorted(self))
