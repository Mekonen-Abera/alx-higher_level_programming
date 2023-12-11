#!/usr/bin/python3
"""
Class definition for Square, inheriting from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square."""
        len_of_args = len(args)
        if len_of_args > 0:
            self.id = args[0]
            len_of_args -= 1
        if len_of_args > 0:
            self.size = args[1]
            len_of_args -= 1
        if len_of_args > 0:
            self.x = args[2]
            len_of_args -= 1
        if len_of_args > 0:
            self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'size':
                    self.width = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        dic2 = {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
        return dic2
