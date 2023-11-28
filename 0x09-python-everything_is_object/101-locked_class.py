#!/usr/bin/python3
"""Define a class LockedClass"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name

    first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new locked class instances."""

        self.first_name = "first_name"
