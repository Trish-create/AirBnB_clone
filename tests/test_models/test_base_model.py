#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def test_create_instance(self):
        """Test creating a BaseModel instance."""
        my_model = BaseModel()

        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_id_is_unique(self):
        """Test that two objects have different IDs."""
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)

    def test_str(self):
        """Test the string representation."""
        my_model = BaseModel()

        self.assertIn("[BaseModel]", str(my_model))
        self.assertIn(my_model.id, str(my_model))

    def test_to_dict(self):
        """Test the to_dict method."""
        my_model = BaseModel()

        my_dict = my_model.to_dict()

        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

    def test_save(self):
        """Test the save method."""
        my_model = BaseModel()

        old_updated_at = my_model.updated_at
        my_model.save()

        self.assertNotEqual(old_updated_at, my_model.updated_at)


if __name__ == "__main__":
    unittest.main()


