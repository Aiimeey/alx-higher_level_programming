#!/usr/bin/python3

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestClassBase(unittest.TestCase):
    """ TestClassBase """
    def test_base_id(self):
        """ Test id zero"""
        Base._Base__nb_objects = 0
        x = Base(0)
        self.assertEqual(x.id, 0)

    def test_empty_dict(self):
        """Test empty dict"""
        dic = Base.to_json_string([])
        self.assertEqual(dic, "[]")

    def test_dict_none(self):
        """Test dict with none"""
        empty_dic = Base.to_json_string(None)
        self.assertEqual(empty_dic, "[]")

    def test_two_dicts(self):
        """Test"""
        dict1 = {"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}
        dict2 = {"x": 10, "y": 17, "id": 3, "height": 14, "width": 15}
        json_dict2 = Base.to_json_string([dict1, dict2])
        expected_json = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 10, "y": 17, "id": 3, "height": 14, "width": 15}]'
        self.assertEqual(json_dict2, expected_json)

    def test_type(self):
        """ test type """
        input = [{'id': 7, 'width': 10, 'height': 4}]
        js_list = Rectangle.to_json_string(input)
        output = Rectangle.from_json_string(js_list)
        self.assertEqual(list, type(output))

    def test_rectangle(self):
        """Test rectangle"""
        input = [{'id': 8, 'width': 11, 'height': 4}]
        js_list = Rectangle.to_json_string(input)
        output = Rectangle.from_json_string(js_list)
        self.assertEqual(input, output)

    def test_square(self):
        """Test square """
        list_input = [{'id': 9, 'size': 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_mul_rectangle(self):
        """Test mul rectangle"""
        input = [
            {'id': 9, 'width': 12, 'height': 4},
            {'id': 8, 'width': 1, 'height': 2}
        ]
        js_list = Rectangle.to_json_string(input)
        output = Rectangle.from_json_string(js_list)
        self.assertEqual(input, output)

    def test_mul_square(self):
        """Test mul square"""
        list_input = [
            {'id': 89, 'size': 4},
            {'id': 98, 'size': 8}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_mul_empty(self):
        """Test mul empty"""
        self.assertEqual([], Base.from_json_string('[]'))

    def test_no_args(self):
        """Test no args"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_many_args(self):
        """Test many args"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 42)

    def test_rect_create(self):
        """Test rect create"""
        dct = {'width': 3, 'height': 4, 'x': 1, 'y': 2, 'id': 42}
        r = Rectangle.create(**dct)
        self.assertDictEqual(r.to_dictionary(), dct)

    def test_square_create(self):
        """Test square create"""
        dct = {'size': 1, 'x': 1, 'y': 2, 'id': 42}
        s = Square.create(**dct)
        self.assertDictEqual(s.to_dictionary(), dct)

    def test_Rect(self):
        """Test rectange"""
        r1 = Rectangle(2, 9, 1, 2, 44)
        r2 = Rectangle(1, 2, 8, 4, 22)
        Rectangle.save_to_file([r1, r2])
        ls = Rectangle.load_from_file()
        self.assertDictEqual(ls[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(ls[0]), Rectangle)
        self.assertDictEqual(ls[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(ls[1]), Rectangle)

    def test_square(self):
        """Test square"""
        s1 = Square(2, 1, 2, 42)
        s2 = Square(4, 2, 1, 24)
        Square.save_to_file([s1, s2])
        ls = Square.load_from_file()
        self.assertDictEqual(ls[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(ls[0]), Square)
        self.assertDictEqual(ls[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(ls[0]), Square)

    def test_no_File(self):
        """Test no file"""
        r = []
        Rectangle.save_to_file(r)
        ls = Rectangle.load_from_file()
        self.assertEqual(ls, [])


if __name__ == '__main__':
    unittest.main()
