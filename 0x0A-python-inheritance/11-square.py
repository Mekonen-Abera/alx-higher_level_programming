#!/usr/bin/python3
"""A Square class Module that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defining A Square class"""
    def __init__(self, size):
        """Initializing a square method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Method that returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
