#!/usr/bin/python3
"""import unittest """
import unittest
from io import StringIO
from unittest import TestCase, mock
from models.square import Square
from models.base import Base


class TestSquare(TestCase):
    """Test the Square class"""

    def test_empty_constructor(self):
        """Test creating a Square with no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_constructor_with_args(self):
        """Test creating a Square with arguments"""
        Base._Base__nb_objects = 0
        s = Square(4)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 4")
        self.assertAlmostEqual(s.area(), 16)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            s.display()
            self.assertEqual(output.getvalue(), "####\n####\n####\n####\n")

    def test_constructor_with_size_x_y_id(self):
        """Test creating a Square with size, x, y, and id"""
        Base._Base__nb_objects = 0
        s = Square(5, 2, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 2/1 - 5")
        self.assertAlmostEqual(s.area(), 25)
        with mock.patch('sys.stdout', new=StringIO()) as output:
            s.display()
            expected_output = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_invalid_arguments(self):
        """Test passing too many arguments or None"""
        with self.assertRaises(TypeError):
            Square(1, 2, 4, 5, 6)

        with self.assertRaises(TypeError):
            Square(None)

    def test_getters_and_setters(self):
        """Test getters and setters"""
        Base._Base__nb_objects = 0
        s = Square(4)
        self.assertAlmostEqual(s.size, 4)
        self.assertAlmostEqual(s.width, 4)
        self.assertAlmostEqual(s.height, 4)

        with self.assertRaises(AttributeError):
            s.__width

        s.size = 22
        self.assertAlmostEqual(s.size, 22)
        self.assertAlmostEqual(s.area(), 484)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 22")

        s = Square(3, 4, 5, 6)
        self.assertAlmostEqual(s.x, 4)
        self.assertAlmostEqual(s.y, 5)
        self.assertAlmostEqual(s.id, 6)

    def test_area(self):
        """Test the area method"""
        self.assertAlmostEqual(Square(2, 0, 0, 1).area(), 4)
        self.assertAlmostEqual(Square(6, 0, 0, 1).area(), 36)

        with self.assertRaises(TypeError):
            Square(1, 0, 0, 1).area("test")

    def test_display(self):
        """Test the display method"""
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(3, 0, 0, 12).display()
            self.assertEqual(output.getvalue(), "###\n###\n###\n")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2, 0, 2, 12).display()
            self.assertEqual(output.getvalue(), "\n\n##\n##\n")

        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(3, 2, 2).display()
            expected_output = "\n\n  ###\n  ###\n  ###\n"
            self.assertEqual(output.getvalue(), expected_output)

        with self.assertRaises(TypeError):
            Square(3, 0, 2, 12).display(5)

    def test_update_args(self):
        """Test the update method with positional arguments"""
        Base._Base__nb_objects = 0
        s5 = Square(2, 3, 4, 5)
        s5.update()
        self.assertEqual(str(s5), "[Square] (5) 3/4 - 2")

        s6 = Square(1, 2, 4, 5)
        s6.update(5, 4, 2, 1, 9)
        self.assertEqual(str(s6), "[Square] (5) 2/1 - 4")

    def test_update_kwargs(self):
        """Test the update method with keyword arguments"""
        s9 = Square(2, 0, 0, 11)
        s9.update()
        self.assertEqual(str(s9), "[Square] (11) 0/0 - 2")

        s12 = Square(2, 0, 0, 11)
        s12.update(x=3, width=11, id=2, height=22)
        self.assertEqual(str(s12), "[Square] (2) 3/0 - 11")

        s12 = Square(2, 0, 0, 11)
        s12.update(x=3, width=11, y=2, id=9, height=22)
        self.assertEqual(str(s12), "[Square] (9) 3/2 - 11")

        s12 = Square(1, 0, 0, 1)
        s12.update(11, 33, 44, 55, x=2, width=3, y=4, id=5, height=6)
        self.assertEqual(str(s12), "[Square] (11) 44/55 - 33")

        s12 = Square(1, 0, 0, 1)
        s12.update(test=1000, e=1001, med=1002, x1=1002, y2=1003)
        self.assertEqual(str(s12), "[Square] (1) 0/0 - 1")

        with self.assertRaises(TypeError):
            r = Square(1, 2, 3, 4)
            r.update(1, [1, 2])

        with self.assertRaises(ValueError):
            r = Square(1, 2, 3, 4)
            r.update(1, -1)

        with self.assertRaises(TypeError):
            r = Square(1, 2, 3, 4)
            r.update(size=(1, 2))

        with self.assertRaises(ValueError):
            r = Square(1, 2, 3, 4)
            r.update(size=-1)


if __name__ == '__main__':
    unittest.main()
