#!/usr/bin/python3
""" Write a class MyList that inherits from list:
   that prints the list, but sorted (ascending sort)
   assume that all the elements of the list will be of type int"""


class MyList(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
