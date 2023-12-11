#!/usr/bin/python3
"""
Unittests for Rectangle Class Attributes
"""

import unittest
import json
import sys
from os import path, remove
import os
from io import StringIO
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # Create instances of the Rectangle class for testing
        self.rect1 = Rectangle(1, 2)
        self.rect2 = Rectangle(5, 2)
        self.rect3 = Rectangle(10, 3, 1, 0, 5)
        self.rect4 = Rectangle(10, 3, 4, 0, 0)
        self.rect5 = Rectangle(1, 1)
        self.rect6 = Rectangle(2, 2)

    def tearDown(self):
        # Delete instances of the Rectangle class after testing
        del self.rect1
        del self.rect2
        del self.rect3
        del self.rect4
        del self.rect5
        del self.rect6
        Base.__Base__nb_objects = 0

    def test_instance(self):
        # Test instantiation of Rectangle instances
        x = self.rect1.id
        self.assertEqual(self.rect1.id, x)
        self.assertEqual(self.rect4.id, 0)
        self.assertIsNot(self.rect1, Base)
        self.assertIsInstance(self.rect1, Base)
        self.assertNotEqual(self.rect1.id, self.rect2.id)
        self.assertEqual(self.rect3.id, 5)
        with self.assertRaises(TypeError):
            r_mthan5 = Rectangle(5, 2, 3, 2, 1, 4)

    def test_attributes_assignment(self):
        # Test attribute assignments of Rectangle instances
        self.assertEqual(self.rect3.width, 10)
        self.assertEqual(self.rect3.height, 3)
        self.assertEqual(self.rect3.x, 1)
        self.assertEqual(self.rect3.y, 0)
        with self.assertRaises(TypeError):
            r = Rectangle(x=1, y=1)

    def test_private_cls(self):
        # Test access to private class attribute
        with self.assertRaises(AttributeError):
            print(self.rect3.__nb_objects)

    def test_private_instance_atr(self):
        # Test access to private instance attributes
        with self.assertRaises(AttributeError):
            print(self.rect3.__width)
        with self.assertRaises(AttributeError):
            print(self.rect3.__height)
        with self.assertRaises(AttributeError):
            print(self.rect3.__x)
        with self.assertRaises(AttributeError):
            print(self.rect3.__y)

    def test_public_instance_atr(self):
        # Test access and modification of public instance attributes
        test_id = Rectangle(10, 12, 1, 2, 6)
        test_id.id = 200

    def test_negative_val(self):
        # Test instantiation with negative values
        with self.assertRaises(ValueError):
            r_negative = Rectangle(-2, 3, 4, 5)
        with self.assertRaises(Exception) as e:
            Rectangle(-2, 3, 4, 5)
        self.assertTrue('width must be > 0' in str(e.exception))

        with self.assertRaises(ValueError):
            r_negative = Rectangle(2, -3, 4, 5)
        with self.assertRaises(Exception) as e:
            Rectangle(2, -3, 4, 5)
        self.assertTrue('height must be > 0' in str(e.exception))

        with self.assertRaises(ValueError):
            r_negative = Rectangle(2, 3, -4, 5)
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, -4, 5)
        self.assertTrue('x must be >= 0' in str(e.exception))

        with self.assertRaises(ValueError):
            r_negative = Rectangle(2, 3, 4, -5)
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, 4, -5)
        self.assertTrue('y must be >= 0' in str(e.exception))

    def test_other_input(self):
        # Test instantiation with invalid input types
        with self.assertRaises(Exception) as e:
            Rectangle("karen", 3, 4, 5)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, {2, 1}, 4, 5)
        self.assertTrue('height must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, [1], 5)
        self.assertTrue('x must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, 3, 4, 5.1)
        self.assertTrue('y must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(float('-inf'), 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(float('NaN'), 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(4.5, 2, 0, 0)
        self.assertTrue('width must be an integer' in str(e.exception))
        with self.assertRaises(Exception) as e:
            Rectangle(2, 2.0, 0, 0)
        self.assertTrue('height must be an integer' in str(e.exception))

    def test_num_attributes(self):
        # Test instantiation with different numbers of attributes
        with self.assertRaises(TypeError):
            r_uno = Rectangle(5)
        r_dos = Rectangle(5, 4)
        self.assertEqual(r_dos.width, 5)
        self.assertEqual(r_dos.height, 4)
        r_tres = Rectangle(5, 4, 3)
        self.assertEqual(r_tres.x, 3)
        self.assertEqual(r_tres.y, 0)
        r_cuatro = Rectangle(5, 4, 3, 1)
        self.assertEqual(r_cuatro.y, 1)

    def test_public_methods(self):
        # Test modification of public methods
        self.rect1.width = 10
        self.rect1.height = 5
        self.rect1.x = 2
        self.rect1.y = 3
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 5)
        self.assertEqual(self.rect1.x, 2)
        self.assertEqual(self.rect1.y, 3)

    def test_area(self):
        # Test the area calculation method
        x = Rectangle(3, 2)
        self.assertEqual(x.area(), 6)

    def test_display(self):
        # Test the display method
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()

    def test_str(self):
        # Test the string representation method
        new = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(new), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        # Test the update method
        new = Rectangle(4, 6, 2, 1, 12)
        new.update(89)
        self.assertEqual(str(new), "[Rectangle] (89) 2/1 - 4/6")
        new.update(89, 2)
        self.assertEqual(str(new), "[Rectangle] (89) 2/1 - 2/6")
        new.update(89, 2, 3)
        self.assertEqual(str(new), "[Rectangle] (89) 2/1 - 2/3")
        new.update(89, 2, 3, 4)
        self.assertEqual(str(new), "[Rectangle] (89) 4/1 - 2/3")
        new.update(89, 2, 3, 4, 6)
        self.assertEqual(str(new), "[Rectangle] (89) 4/6 - 2/3")

    def test_update_1(self):
        # Test the update method with named arguments
        new = Rectangle(1, 1, 1, 1, 50)

        new.update(height=2)
        self.assertEqual(str(new), "[Rectangle] (50) 1/1 - 1/2")

        new.update(width=8, x=7)
        self.assertEqual(str(new), "[Rectangle] (50) 7/1 - 8/2")

        new.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(new), "[Rectangle] (89) 3/1 - 2/2")

        new.update(8, width=5)
        self.assertEqual(str(new), "[Rectangle] (8) 3/1 - 5/2")

    def test_to_dictionary(self):
        # Test the to_dictionary method
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)
        r = Rectangle(1, 2, 0, 0, 1)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

    if __name__ == '__main__':
        unittest.main()

