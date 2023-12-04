#!/usr/bin/python3
"""Define a class MyList that inherits from list"""


class MyList(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
