#!/usr/bin/python3
"""
Defines unittests for models/Square.py.
"""
import unittest
from models.square import Square

class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for testing the update method with arguments of the Square class."""

    def test_update_args_zero(self):
        # Test update with zero arguments.
        square = Square(10, 10, 10, 10)
        square.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(square))

    def test_update_args_one(self):
        # Test update with one argument.
        square = Square(10, 10, 10, 10)
        square.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(square))

    def test_update_args_two(self):
        # Test update with two arguments.
        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(square))

    def test_update_args_three(self):
        # Test update with three arguments.
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(square))

    def test_update_args_four(self):
        # Test update with four arguments.
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(square))

    def test_update_args_more_than_four(self):
        # Test update with more than four arguments.
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(square))

    def test_update_args_width_setter(self):
        # Test if width is correctly set using update.
        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual(2, square.width)

    def test_update_args_height_setter(self):
        # Test if height is correctly set using update.
        square = Square(10, 10, 10, 10)
        square.update(89, 2)
        self.assertEqual(2, square.height)

    def test_update_args_None_id(self):
        # Test update with None as the first argument.
        square = Square(10, 10, 10, 10)
        square.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(square.id)
        self.assertEqual(correct, str(square))

    def test_update_args_None_id_and_more(self):
        # Test update with None as the first argument and more arguments.
        square = Square(10, 10, 10, 10)
        square.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(square.id)
        self.assertEqual(correct, str(square))

    def test_update_args_twice(self):
        # Test update with multiple sets of arguments.
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)
        square.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(square))

    def test_update_args_invalid_size_type(self):
        # Test update with invalid size type.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid")

    def test_update_args_size_zero(self):
        # Test update with size set to zero.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, 0)

    def test_update_args_size_negative(self):
        # Test update with negative size.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, -4)

    def test_update_args_invalid_x(self):
        # Test update with invalid x type.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        # Test update with negative x.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        # Test update with invalid y type.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        # Test update with negative y.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        # Test update with size before x.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        # Test update with size before y.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        # Test update with x before y.
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 1, "invalid", "invalid")

if __name__ == "__main__":
    unittest.main()

