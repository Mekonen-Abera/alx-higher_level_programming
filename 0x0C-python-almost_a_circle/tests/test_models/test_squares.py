#!/usr/bin/python3
'''A Module for the Square unittests'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io

class TestSquare(unittest.TestCase):
    '''Define the Tests for the Base class'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass


    def test_A_class(self):
        '''Tests Square class type.'''
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Tests if Square inherits Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 were given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Tests instantiation.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Tests positional instantiation.'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Tests positional instantiation.'''
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Tests if id is inherited from Base.'''
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''Tests property getters/setters.'''
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)


    def invalid_types(self):
        '''Returns tuple of types for validation.'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Tests property validation.'''
        r = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''Tests property validation.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''Tests property setting/getting.'''
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''Tests property setting/getting.'''
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_I_area_no_args(self):
        '''Tests area() method signature.'''
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() method computation.'''
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) + 1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_J_display_no_args(self):
        '''Tests display() method signature.'''
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)
    def test_display_simple(self):
        """Tests the display() method output."""
        # Test case 1: Square of size 1
        square1 = Square(1)
        output1 = io.StringIO()
        with redirect_stdout(output1):
            square1.display()
        expected_output1 = "#\n"
        self.assertEqual(output1.getvalue(), expected_output1)

        # Test case 2: Square of size 3
        square2 = Square(3)
        output2 = io.StringIO()
        with redirect_stdout(output2):
            square2.display()
        expected_output2 = "###\n###\n###\n"
        self.assertEqual(output2.getvalue(), expected_output2)

        # Test case 3: Square of size 5 with offset (6, 7)
        square3 = Square(5, 6, 7)
        output3 = io.StringIO()
        with redirect_stdout(output3):
            square3.display()
        expected_output3 = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(output3.getvalue(), expected_output3)

        # Test case 4: Square of size 9 with offset (8, 0)
        square4 = Square(9, 8)
        output4 = io.StringIO()
        with redirect_stdout(output4):
            square4.display()
        expected_output4 = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(output4.getvalue(), expected_output4)

        # Test case 5: Square of size 1 with offset (1, 10)
        square5 = Square(1, 1, 10)
        output5 = io.StringIO()
        with redirect_stdout(output5):
            square5.display()
        expected_output5 = """\










 #
"""
        self.assertEqual(output5.getvalue(), expected_output5)

        # Test case 6: Square of size 5 with no offset
        square6 = Square(5)
        output6 = io.StringIO()
        with redirect_stdout(output6):
            square6.display()
        expected_output6 = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(output6.getvalue(), expected_output6)

        # Test case 7: Square of size 5 with offset (5, 5)
        square7 = Square(5, 5)
        output7 = io.StringIO()
        with redirect_stdout(output7):
            square7.display()
        expected_output7 = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(output7.getvalue(), expected_output7)

        # Test case 8: Square of size 5 with offset (3, 0)
        square8 = Square(5, 3)
        output8 = io.StringIO()
        with redirect_stdout(output8):
            square8.display()
        expected_output8 = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(output8.getvalue(), expected_output8)

        # Test case 9: Square of size 5 with offset (0, 4)
        square9 = Square(5, 0, 4)
        output9 = io.StringIO()
        with redirect_stdout(output9):
            square9.display()
        expected_output9 = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(output9.getvalue(), expected_output9)

        Base._Base__nb_objects = 0
        square10 = Square(5)
        self.assertEqual(str(square10), "[Square] (1) 0/0 - 5")
        self.assertEqual(square10.area(), 25)
        output10 = io.StringIO()
        with redirect_stdout(output10):
            square10.display()
        expected_output10 = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(output10.getvalue(), expected_output10)

        square11 = Square(2, 2)
        self.assertEqual(str(square11), "[Square] (2) 2/0 - 2")
        self.assertEqual(square11.area(), 4)
        output11 = io.StringIO()
        with redirect_stdout(output11):
            square11.display()
        expected_output11 = """\
  ##
  ##
"""
        self.assertEqual(output11.getvalue(), expected_output11)

        square12 = Square(3, 1, 3)
        self.assertEqual(str(square12), "[Square] (3) 1/3 - 3")
        self.assertEqual(square12.area(), 9)
        output12 = io.StringIO()
        with redirect_stdout(output12):
            square12.display()
        expected_output12 = """\



 ###
 ###
 ###
"""
        self.assertEqual(output12.getvalue(), expected_output12)

    def test_str_no_args(self):
        """Tests __str__() method signature."""
        square = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        expected_error = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), expected_error)

    def test_str(self):
        """Tests __str__() method return."""
        square1 = Square(5)
        expected_str1 = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(square1), expected_str1)

        square2 = Square(1, 1)
        expected_str2 = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(square2), expected_str2)

        square3 = Square(3, 4, 5)
        expected_str3 = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(square3), expected_str3)

        square4 = Square(10, 20, 30, 40)
        expected_str4 = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(square4), expected_str4)
def test_update_no_args(self):
        '''Tests update() method signature.'''
        square = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        expected_error = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), expected_error)

        # Check if update with no arguments doesn't modify the Square
        square_dict = square.__dict__.copy()
        square.update()
        self.assertEqual(square.__dict__, square_dict)

    def test_update_args(self):
        '''Tests update() positional args.'''
        square = Square(5, 2)
        square_dict = square.__dict__.copy()

        # Check if update modifies the Square with different positional arguments
        square.update(10)
        square_dict["id"] = 10
        self.assertEqual(square.__dict__, square_dict)

        square.update(10, 5)
        square_dict["_Rectangle__height"] = 5
        square_dict["_Rectangle__width"] = 5
        self.assertEqual(square.__dict__, square_dict)

        square.update(10, 5, 20)
        square_dict["_Rectangle__x"] = 20
        self.assertEqual(square.__dict__, square_dict)

        square.update(10, 5, 20, 25)
        square_dict["_Rectangle__y"] = 25
        self.assertEqual(square.__dict__, square_dict)

    def test_update_args_bad(self):
        '''Tests update() positional arg fubars.'''
        square = Square(5, 2)
        square_dict = square.__dict__.copy()

        # Check if update with negative width raises ValueError
        square.update(10)
        square_dict["id"] = 10
        self.assertEqual(square.__dict__, square_dict)

        with self.assertRaises(ValueError) as e:
            square.update(10, -5)
        expected_error = "width must be > 0"
        self.assertEqual(str(e.exception), expected_error)

        # Check if update with negative x raises ValueError
        with self.assertRaises(ValueError) as e:
            square.update(10, 5, -17)
        expected_error = "x must be >= 0"
        self.assertEqual(str(e.exception), expected_error)

        # Check if update with negative y raises ValueError
        with self.assertRaises(ValueError) as e:
            square.update(10, 5, 17, -25)
        expected_error = "y must be >= 0"
        self.assertEqual(str(e.exception), expected_error)

    def test_update_kwargs(self):
        '''Tests update() keyword args.'''
        square = Square(5, 2)
        square_dict = square.__dict__.copy()

        # Check if update modifies the Square with different keyword arguments
        square.update(id=10)
        square_dict["id"] = 10
        self.assertEqual(square.__dict__, square_dict)

        square.update(size=17)
        square_dict["_Rectangle__height"] = 17
        square_dict["_Rectangle__width"] = 17
        self.assertEqual(square.__dict__, square_dict)

        square.update(x=20)
        square_dict["_Rectangle__x"] = 20
        self.assertEqual(square.__dict__, square_dict)

        square.update(y=25)
        square_dict["_Rectangle__y"] = 25
        self.assertEqual(square.__dict__, square_dict)

    def test_update_kwargs_2(self):
        '''Tests update() keyword args.'''
        square = Square(5, 2)
        square_dict = square.__dict__.copy()

        # Check if update modifies the Square with different keyword arguments
        square.update(id=10)
        square_dict["id"] = 10
        self.assertEqual(square.__dict__, square_dict)

        square.update(id=10, size=5)
        square_dict["_Rectangle__height"] = 5
        square_dict["_Rectangle__width"] = 5
        self.assertEqual(square.__dict__, square_dict)

        square.update(id=10, size=5, x=20)
        square_dict["_Rectangle__x"] = 20
        self.assertEqual(square.__dict__, square_dict)

        square.update(id=10, size=5, x=20, y=25)
        square_dict["_Rectangle__y"] = 25
        self.assertEqual(square.__dict__, square_dict)

        # Check if update ignores unexpected keyword arguments
        square.update(y=25, id=10, x=20, size=5)
        self.assertEqual(square.__dict__, square_dict)

        # Resetting the counter for Base class
        Base._Base__nb_objects = 0

        # Create a Square instance
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        # Check if update modifies the Square with different positional arguments
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        # Check if update modifies the Square with different keyword arguments
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        '''Tests to_dictionary() signature:'''
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        expected_error = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), expected_error)

        # Check if to_dictionary returns the expected dictionary
        square = Square(1)
        expected_dict = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(square.to_dictionary(), expected_dict)

        square = Square(9, 2, 3, 4)
        expected_dict = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(square.to_dictionary(), expected_dict)

        # Modify Square properties and check if to_dictionary returns the expected dictionary
        square.x = 10
        square.y = 20
        square.size = 30
        expected_dict = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(square.to_dictionary(), expected_dict)

        # Check if to_dictionary creates a dictionary that can be used to recreate the Square
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

if __name__ == "__main__":
    unittest.main()
