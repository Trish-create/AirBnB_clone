#!/usr/bin/python3
"""Tests for BaseModel."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def test_create_instance(self):
        """Test creating a BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)


if __name__ == "__main__":
    unittest.main()
