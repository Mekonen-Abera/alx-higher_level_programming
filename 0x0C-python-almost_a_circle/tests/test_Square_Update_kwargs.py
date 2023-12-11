#!/usr/bin/python3

"""Defines unittests for models/square.py."""

import io
import sys
import unittest
from models.base import Base
from models.square import Square

class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for testing the update method with keyword arguments of Square class."""

    def test_update_kwargs_one(self):
        # Test updating with one keyword argument.
        square = Square(10, 10, 10, 10)
        square.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(square))

    def test_update_kwargs_two(self):
        # Test updating with two keyword arguments.
        square = Square(10, 10, 10, 10)
        square.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(square))

    def test_update_kwargs_three(self):
        # Test updating with three keyword arguments.
        square = Square(10, 10, 10, 10)
        square.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(square))

    def test_update_kwargs_four(self):
        # Test updating with four keyword arguments.
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(square))

    def test_update_kwargs_width_setter(self):
        # Test updating width using a keyword argument.
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=8)
        self.assertEqual(8, square.width)

    def test_update_kwargs_height_setter(self):
        # Test updating height using a keyword argument.
        square = Square(10, 10, 10, 10)
        square.update(id=89, size=9)
        self.assertEqual(9, square.height)

    def test_update_kwargs_None_id(self):
        # Test updating with None as the id keyword argument.
        square = Square(10, 10, 10, 10)
        square.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(square.id)
        self.assertEqual(correct, str(square))

    def test_update_kwargs_None_id_and_more(self):
        # Test updating with None as the id keyword argument and additional arguments.
        square = Square(10, 10, 10, 10)
        square.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(square.id)
        self.assertEqual(correct, str(square))

    def test_update_kwargs_twice(self):
        # Test updating with keyword arguments multiple times.
        square = Square(10, 10, 10, 10)
        square.update(id=89, x=1)
        square.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(square))

    def test_update_kwargs_invalid_size(self):
        # Test updating with invalid size type.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        # Test updating with size set to zero.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=0)

    def test_update_kwargs_size_negative(self):
        # Test updating with negative size.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        # Test updating with invalid x type.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        # Test updating with negative x.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        # Test updating with invalid y type.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        # Test updating with negative y.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(y=-5)

    def test_update_args_and_kwargs(self):
        # Test updating with both args and kwargs, where kwargs take precedence.
        square = Square(10, 10, 10, 10)
        square.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(square))

    def test_update_kwargs_wrong_keys(self):
        # Test updating with invalid keyword arguments.
        square = Square(10, 10, 10, 10)
        square.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(square))

    def test_update_kwargs_some_wrong_keys(self):
        # Test updating with some valid and some invalid keyword arguments.
        square = Square(10, 10, 10, 10)
        square.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(square))

if __name__ == "__main__":
    unittest.main()

