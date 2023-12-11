#!/usr/bin/python3
"""
Define a Rectangle module inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter method for x-coordinate.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x-coordinate.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for y-coordinate.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y-coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        area = self.width * self.height

        return area

    def display(self):
        """
        Prints the rectangle using '#' symbols.
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns the string representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes based on their positions.
        """
        if args:
            for count, arg in enumerate(args):
                setattr(self, self._update_order[count], arg)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Represents a dictionary representation of the rectangle.
        """
        rec_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        return rec_dict


if __name__ == "__main__":
    pass
