#!/usr/bin/python3
"""
Unit tests Review Class
"""
from models.review import Review
from models.user import User
from models.place import Place
import unittest
from datetime import datetime
import pycodestyle


class TestReview(unittest.TestCase):
    """
    Unit tests Review Class
    """

    def test_style_check(self):
        """
        Test if the code pass the pycodestyle
        """
        style = pycodestyle.StyleGuide()
        checker = style.check_files(['models/review.py'])
        self.assertEqual(checker.total_errors, 0, "fix pycodestyle")

    def test_functions_documentation(self):
        """
        Test if the documentation for each function exist
        """
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_word_count_documentation(self):
        """
        Test if the documentation is 10 chars of bigger
        """
        n = len(Review.__doc__)
        self.assertGreaterEqual(n, 10)
        m = len(Review.__init__.__doc__)
        self.assertGreaterEqual(m, 10)

    def setUp(self):
        """
        Initialization
        """
        self.place = Place()
        self.user = User()
        self.rev_1 = Review()
        self.rev_1.place_id = self.place.id
        self.rev_1.user_id = self.user.id
        self.rev_1.text = "Nice view"
        self.rev_2 = Place()

    def test_base_attribute(self):
        """
        Test attribute BaseModel
        """
        self.assertIsNotNone(self.rev_1.id)
        self.assertIsNotNone(self.rev_1.created_at)
        self.assertIsNotNone(self.rev_1.updated_at)

    def test_base_type(self):
        """
        Test type attribute BaseModel
        """
        self.assertEqual(type(self.rev_1.id), str)
        self.assertEqual(type(self.rev_1.created_at), datetime)
        self.assertEqual(type(self.rev_1.updated_at), datetime)

    def test_review_attributes(self):
        """
        Test attribute Review Class
        """
        self.assertEqual(self.rev_1.text, "Nice view")
        self.assertEqual(self.rev_1.place_id, self.place.id)
        self.assertEqual(self.rev_1.user_id, self.user.id)

    def test_no_arg(self):
        """
        Test Review class with no attributes
        """
        self.assertEqual(self.rev_2.name, "")

    def test_review_type(self):
        """
        Test type attribute Review Class
        """
        self.assertEqual(type(self.rev_2.name), str)

    def test_attributes(self):
        """
        Test instance attributes
        """
        rev = Review()
        place_id = getattr(rev, "place_id")
        user_id = getattr(rev, "user_id")
        text = getattr(rev, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)


if __name__ == '__main__':
    unittest.main()
