#!/usr/bin/python3

"""Defines unittests for models/square.py."""

import io
import sys
import unittest
from models.base import Base
from models.square import Square

class TestSquareToDictionary(unittest.TestCase):
    """Unittests for testing the to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        # Ensure to_dictionary returns the correct dictionary representation.
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        # Ensure updating another Square with the dictionary does not modify the original object.
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        # Ensure TypeError is raised when passing an argument to to_dictionary.
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()

