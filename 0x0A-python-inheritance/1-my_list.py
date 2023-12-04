#!/usr/bin/python3
""" Write a class MyList that inherits from list:
   that prints the list, but sorted (ascending sort)
   assume that all the elements of the list will be of type int
"""

class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """Print the list in ascending sorted"""
        print(sorted(self))
