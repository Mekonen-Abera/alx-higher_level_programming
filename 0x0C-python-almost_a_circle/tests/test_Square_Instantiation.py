#!/usr/bin/python3

"""Defines unittests for models/square.py."""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Tests for creating instances of the Square class."""

    def test_is_base_instance(self):
        # Verify that an instance of Square is an instance of Base.
        self.assertIsInstance(Square(10), Base)

    def test_is_square_instance(self):
        # Verify that an instance of Square is an instance of Square itself.
        self.assertIsInstance(Square(10), Square)

    def test_no_arguments(self):
        # Ensure an error is raised when creating a Square instance with no arguments.
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        # Check if two consecutive squares have consecutive IDs.
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_arguments(self):
        # Verify that the ID of the square created with (10, 2) is one less than (2, 10).
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_arguments(self):
        # Verify that the ID of the square created with (10, 2, 2) is one less than (2, 2, 10).
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_arguments(self):
        # Verify that the ID of the square created with (10, 2, 2, 7) is 7.
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_arguments(self):
        # Ensure an error is raised when creating a Square with more than four arguments.
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_private_size_attribute(self):
        # Ensure AttributeError is raised when trying to access the private __size attribute.
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        # Verify that the size getter returns the correct size.
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        # Verify that the size setter updates the size correctly.
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        # Verify that the width getter returns the correct width.
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        # Verify that the height getter returns the correct height.
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        # Verify that the x getter returns 0 for a Square with only size provided.
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        # Verify that the y getter returns 0 for a Square with only size provided.
        self.assertEqual(0, Square(10).y)


class TestSquareSizeInitialization(unittest.TestCase):
    """Tests for initializing the size attribute of the Square class."""

    def test_none_size(self):
        # Ensure TypeError is raised when size is None.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        # Ensure TypeError is raised when size is a string.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        # Ensure TypeError is raised when size is a float.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        # Ensure TypeError is raised when size is a complex number.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        # Ensure TypeError is raised when size is a dictionary.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        # Ensure TypeError is raised when size is a boolean.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        # Ensure TypeError is raised when size is a list.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        # Ensure TypeError is raised when size is a set.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        # Ensure TypeError is raised when size is a tuple.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        # Ensure TypeError is raised when size is a frozenset.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        # Ensure TypeError is raised when size is a range object.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        # Ensure TypeError is raised when size is bytes.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        # Ensure TypeError is raised when size is a bytearray.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        # Ensure TypeError is raised when size is a memoryview.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        # Ensure TypeError is raised when size is infinity.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        # Ensure TypeError is raised when size is NaN.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        # Ensure ValueError is raised when size is negative.
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        # Ensure ValueError is raised when size is zero.
            Square(0, 2)


class TestSquareX(unittest.TestCase):
    """Tests for initializing the x attribute of the Square class."""

    def test_none_x(self):
        # Ensure TypeError is raised when x is None.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        # Ensure TypeError is raised when x is a string.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        # Ensure TypeError is raised when x is a float.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        # Ensure TypeError is raised when x is a complex number.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        # Ensure TypeError is raised when x is a dictionary.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        # Ensure TypeError is raised when x is a boolean.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        # Ensure TypeError is raised when x is a list.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        # Ensure TypeError is raised when x is a set.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        # Ensure TypeError is raised when x is a tuple.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        # Ensure TypeError is raised when x is a frozenset.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        # Ensure TypeError is raised when x is a range object.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        # Ensure TypeError is raised when x is bytes.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_bytearray_x(self):
        # Ensure TypeError is raised when x is a bytearray.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        # Ensure TypeError is raised when x is a memoryview.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def test_inf_x(self):
        # Ensure TypeError is raised when x is infinity.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        # Ensure TypeError is raised when x is NaN.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def test_negative_x(self):
        # Ensure ValueError is raised when x is negative.
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquareY(unittest.TestCase):
    """Tests for initializing the y attribute of the Square class."""

    def test_none_y(self):
        # Ensure TypeError is raised when y is None.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        # Ensure TypeError is raised when y is a string.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        # Ensure TypeError is raised when y is a float.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complex_y(self):
        # Ensure TypeError is raised when y is a complex number.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dict_y(self):
        # Ensure TypeError is raised when y is a dictionary.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        # Ensure TypeError is raised when y is a list.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        # Ensure TypeError is raised when y is a set.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuple_y(self):
        # Ensure TypeError is raised when y is a tuple.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozenset_y(self):
        # Ensure TypeError is raised when y is a frozenset.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        # Ensure TypeError is raised when y is a range object.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytes_y(self):
        # Ensure TypeError is raised when y is bytes.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    def test_bytearray_y(self):
        # Ensure TypeError is raised when y is a bytearray.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        # Ensure TypeError is raised when y is a memoryview.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        # Ensure TypeError is raised when y is infinity.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        # Ensure TypeError is raised when y is NaN.
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_negative_y(self):
        # Ensure ValueError is raised when y is negative.
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)

class TestSquareOrderOfInitialization(unittest.TestCase):
    """Tests for checking the order of Square attribute initialization."""

    def test_size_before_x(self):
        # Ensure TypeError is raised when size and x are invalid types.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        # Ensure TypeError is raised when size and y are invalid types.
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        # Ensure TypeError is raised when x and y are invalid types.
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquareArea(unittest.TestCase):
    """Tests for the area method of the Square class."""

    def test_area_small(self):
        # Ensure area is calculated correctly for a small square.
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        # Ensure area is calculated correctly for a large square.
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        # Ensure area is updated correctly when attributes are changed.
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_one_arg(self):
        # Ensure TypeError is raised when passing an argument to area.
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquareStdout(unittest.TestCase):
    """Tests for the __str__ and display methods of the Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.
        Args:
            sq (Square): The Square object to print to stdout.
            method (str): The method to run on sq ("print" or "display").
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        # Ensure __str__ method prints correct information for size.
        s = Square(4)
        capture = TestSquareStdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        # Ensure __str__ method prints correct information for size and x.
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y(self):
        # Ensure __str__ method prints correct information for size, x, and y.
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        # Ensure __str__ method prints correct information for all attributes.
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        # Ensure __str__ method reflects changes in attributes.
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        # Ensure TypeError is raised when passing an argument to __str__.
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Tests for display method
    def test_display_size(self):
        # Ensure display method prints correct representation for size.
        s = Square(2, 0, 0, 9)
        capture = TestSquareStdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        # Ensure display method prints correct representation for size and x.
        s = Square(3, 1, 0, 18)
        capture = TestSquareStdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        # Ensure display method prints correct representation for size and y.
        s = Square(4, 0, 1, 9)
        capture = TestSquareStdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        # Ensure display method prints correct representation for size, x, and y.
        s = Square(2, 3, 2, 1)
        capture = TestSquareStdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        # Ensure TypeError is raised when passing an argument to display.
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)

if __name__ == "__main__":
    unittest.main()

