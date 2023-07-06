#!/usr/bin/python3
"""
Unit tests Place Class
"""
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
import unittest
from datetime import datetime
import pycodestyle


class TestPlace(unittest.TestCase):
    """
    Unit tests Place Class
    """

    def test_style_check(self):
        """
        Test if the code pass the pycodestyle
        """
        style = pycodestyle.StyleGuide()
        checker = style.check_files(['models/place.py'])
        self.assertEqual(checker.total_errors, 0, "fix pycodestyle")

    def test_functions_documentation(self):
        """
        Test if the documentation for each function exist
        """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_word_count_documentation(self):
        """
        Test if the documentation is 10 chars of bigger
        """
        n = len(Place.__doc__)
        self.assertGreaterEqual(n, 10)
        m = len(Place.__init__.__doc__)
        self.assertGreaterEqual(m, 10)

    def setUp(self):
        """
        Initialization
        """
        self.city = City()
        self.user = User()
        self.amenity = Amenity()
        self.place_1 = Place()
        self.place_1.city_id = self.city.id
        self.place_1.user_id = self.user.id
        self.place_1.name = "Torre Blanca"
        self.place_1.description = "Loft"
        self.place_1.number_rooms = 1
        self.place_1.number_bathrooms = 1
        self.place_1.max_guest = 2
        self.place_1.price_by_night = 50
        self.place_1.latitude = 67.89
        self.place_1.longitude = 123.45
        self.place_1.amenity_ids = [self.amenity]
        self.place_2 = Place()

    def test_base_attribute(self):
        """
        Test BaseModel attributes
        """
        self.assertIsNotNone(self.place_1.id)
        self.assertIsNotNone(self.place_1.created_at)
        self.assertIsNotNone(self.place_1.updated_at)

    def test_base_type(self):
        """
        Test BaseModel type attributea
        """
        self.assertEqual(type(self.place_1.id), str)
        self.assertEqual(type(self.place_1.created_at), datetime)
        self.assertEqual(type(self.place_1.updated_at), datetime)

    def test_place_attribute(self):
        """
        Test class Place attributes
        """
        self.assertEqual(self.place_1.name, "Torre Blanca")
        self.assertEqual(self.place_1.description, "Loft")
        self.assertEqual(self.place_1.city_id, self.city.id)
        self.assertEqual(self.place_1.user_id, self.user.id)
        self.assertEqual(self.place_1.number_rooms, 1)
        self.assertEqual(self.place_1.number_bathrooms, 1)
        self.assertEqual(self.place_1.max_guest, 2)
        self.assertEqual(self.place_1.price_by_night, 50)
        self.assertEqual(self.place_1.latitude, 67.89)
        self.assertEqual(self.place_1.longitude, 123.45)

    def test_no_arg(self):
        """
        Test class Place with no attributes
        """
        self.assertEqual(self.place_2.name, "")
        self.assertEqual(self.place_2.description, "")
        self.assertEqual(self.place_2.city_id, "")
        self.assertEqual(self.place_2.user_id, "")
        self.assertEqual(self.place_2.number_rooms, 0)
        self.assertEqual(self.place_2.number_bathrooms, 0)
        self.assertEqual(self.place_2.max_guest, 0)
        self.assertEqual(self.place_2.price_by_night, 0)
        self.assertEqual(self.place_2.latitude, 0.0)
        self.assertEqual(self.place_2.longitude, 0.0)
        self.assertEqual(self.place_2.amenity_ids, [])

    def test_place_type(self):
        """
        Test type attribute Place
        """
        self.assertEqual(type(self.place_2.name), str)
        self.assertEqual(type(self.place_2.description), str)
        self.assertEqual(type(self.place_2.number_rooms), int)
        self.assertEqual(type(self.place_2.max_guest), int)
        self.assertEqual(type(self.place_2.price_by_night), int)
        self.assertEqual(type(self.place_2.latitude), float)
        self.assertEqual(type(self.place_2.longitude), float)


if __name__ == '__main__':
    unittest.main()
