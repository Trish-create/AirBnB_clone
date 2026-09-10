#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class."""

    def test_create_instance(self):
        """Test creating a Place."""
        place = Place()

        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.id, str)

    def test_attributes(self):
        """Test Place attributes."""
        place = Place()

        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Nice House"
        place.description = "A beautiful house"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 5
        place.price_by_night = 100
        place.latitude = 1.234
        place.longitude = 5.678

        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Nice House")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.price_by_night, 100)


if __name__ == "__main__":
    unittest.main()
