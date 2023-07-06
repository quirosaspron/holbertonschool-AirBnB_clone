#!/usr/bin/python3
"""
Unit tests City class
"""
from models.city import City
from models.state import State
import unittest
from datetime import datetime
import pycodestyle


class TestCity(unittest.TestCase):
    """
    Unit tests City class
    """

    def test_style_check(self):
        """
        Test if the code pass the pycodestyle
        """
        style = pycodestyle.StyleGuide()
        checker = style.check_files(['models/city.py'])
        self.assertEqual(checker.total_errors, 0, "fix pycodestyle")

    def test_functions_documentation(self):
        """
        Test if the documentation for each function exist
        """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_word_count_documentation(self):
        """
        Test if the documentation is 10 chars of bigger
        """
        n = len(City.__doc__)
        self.assertGreaterEqual(n, 10)
        m = len(City.__init__.__doc__)
        self.assertGreaterEqual(m, 10)

    def setUp(self):
        """
        Initialization
        """
        self.city_1 = City()
        self.city_1.name = "Orlando"
        self.state = State()
        self.state.name = "Florida"
        self.city_1.state_id = self.state.id
        self.city_2 = City()

    def test_base_attribute(self):
        """
        Test attribute BaseModel
        """
        self.assertIsNotNone(self.city_1.id)
        self.assertIsNotNone(self.city_1.created_at)
        self.assertIsNotNone(self.city_1.updated_at)

    def test_base_type(self):
        """
        Test type attribute BaseModel
        """
        self.assertEqual(type(self.city_1.id), str)
        self.assertEqual(type(self.city_1.created_at), datetime)
        self.assertEqual(type(self.city_1.updated_at), datetime)

    def test_city_attribute(self):
        """
        Test attribute City class
        """
        self.assertEqual(self.city_1.name, "Orlando")
        self.assertEqual(self.city_1.state_id, self.state.id)

    def test_no_arg(self):
        """
        Test City class with no attributes
        """
        self.assertEqual(self.city_2.name, "")

    def test_city_type(self):
        """
        Test type attribute City class
        """
        self.assertEqual(type(self.city_1.name), str)
        self.assertEqual(type(self.city_1.state_id), str)
        self.assertEqual(type(self.city_2.name), str)


if __name__ == '__main__':
    unittest.main()
