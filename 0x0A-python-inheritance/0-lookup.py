#!/usr/bin/python3
"""A function module with lookup method"""


def lookup(obj):
    """lookup method function
    Returns: a list of available attributes and methods of an object"""
    return dir(obj)
