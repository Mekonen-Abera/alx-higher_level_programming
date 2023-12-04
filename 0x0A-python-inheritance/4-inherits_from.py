#!/usr/bin/python3
"""Define Module containing inherits_from method"""


def inherits_from(obj, a_class):
    """Reurns True if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class ; otherwise False """
    return isinstance(obj, a_class) and type(obj) != a_class
