#!/usr/bin/python3

"""Defines unittests for base.py."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseFromJsonString(unittest.TestCase):
    """Unit tests for the from_json_string method of the Base class."""

    def test_from_json_string_type(self):
        """Test if the output type of from_json_string is a list."""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        """Test the conversion of a JSON string with one Rectangle to a list."""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        """Test the conversion of a JSON string with two Rectangles to a list."""
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        """Test the conversion of a JSON string with one Square to a list."""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        """Test the conversion of a JSON string with two Squares to a list."""
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        """Test if the from_json_string method returns an empty list for None input."""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """Test if the from_json_string method returns an empty list for an empty string."""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Test that from_json_string raises a TypeError when called without arguments."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """Test that from_json_string raises a TypeError when called with more than one argument."""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

if __name__ == "__main__":
    unittest.main()
