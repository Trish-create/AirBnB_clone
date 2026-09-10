#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class."""

    def test_create_instance(self):
        """Test creating an Amenity."""
        amenity = Amenity()

        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.name, str)

    def test_name(self):
        """Test the name attribute."""
        amenity = Amenity()

        amenity.name = "WiFi"

        self.assertEqual(amenity.name, "WiFi")


                                                                                
if __name__ == "__main__":
    unittest.main()
