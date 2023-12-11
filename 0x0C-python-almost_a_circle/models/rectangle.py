#!/usr/bin/python3
"""
Class definition for Rectangle, inheriting from Base.
"""

from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using '#' characters."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end="")
            for _ in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle."""
        len_of_args = len(args)
        if len_of_args > 0:
            self.id = args[0]
            len_of_args -= 1
        if len_of_args > 0:
            self.__width = args[1]
            len_of_args -= 1
        if len_of_args > 0:
            self.__height = args[2]
            len_of_args -= 1
        if len_of_args > 0:
            self.__x = args[3]
            len_of_args -= 1
        if len_of_args > 0:
            self.__y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        dic1 = {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
        return dic1
