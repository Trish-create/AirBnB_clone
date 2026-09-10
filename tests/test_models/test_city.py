#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_create_instance(self):
        """Test creating a City."""
        city = City()

        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_attributes(self):
        """Test City attributes."""
        city = City()

        city.state_id = "1234"
        city.name = "Los Angeles"

        self.assertEqual(city.state_id, "1234")
        self.assertEqual(city.name, "Los Angeles")


                                                                                
if __name__ == "__main__":
    unittest.main()
