#!/usr/bin/python3
"""
Write a function that returns True if the object is exactly 
an instance of the specified class ; otherwise False.
"""

def is_same_class(obj, a_class):
    """Returns:
    True: if the object is exactly an instance of the specified class
    False: otherwise"""
    return type(obj) == a_class
