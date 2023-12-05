#!/usr/bin/python3
"""A function that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
