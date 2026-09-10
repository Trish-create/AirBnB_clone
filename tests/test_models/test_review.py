#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class."""

    def test_create_instance(self):
        """Test creating a Review."""
        review = Review()

        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_attributes(self):
        """Test Review attributes."""
        review = Review()

        review.place_id = "place123"
        review.user_id = "user123"
        review.text = "Great place!"

        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.text, "Great place!")


if __name__ == "__main__":
    unittest.main()
