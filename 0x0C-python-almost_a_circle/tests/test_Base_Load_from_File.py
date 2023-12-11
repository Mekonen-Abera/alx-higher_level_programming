#!/usr/bin/python3

"""Defines unittests for base load from file."""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_argument(self):
        # Test instantiation with no arguments
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        # Test instantiation of three Base instances
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_none_id(self):
        # Test instantiation with None as the id
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        # Test instantiation with a unique id
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        # Test number of instances after instantiation with a unique id
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        # Test public access to the id attribute
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        # Test private access to the __nb_instances attribute
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        # Test instantiation with a string id
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        # Test instantiation with a float id
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        # Test instantiation with a complex id
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        # Test instantiation with a dictionary id
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        # Test instantiation with a boolean id
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        # Test instantiation with a list id
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        # Test instantiation with a tuple id
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        # Test instantiation with a set id
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        # Test instantiation with a frozenset id
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        # Test instantiation with a range id
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        # Test instantiation with a bytes id
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        # Test instantiation with a bytearray id
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        # Test instantiation with a memoryview id
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        # Test instantiation with positive infinity as the id
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        # Test instantiation with NaN as the id
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        # Test instantiation with two arguments
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()
