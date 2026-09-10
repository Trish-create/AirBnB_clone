#!/usr/bin/python3
"""Tests for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class."""

    def test_create_user(self):
        """Test creating a User."""
        user = User()

        self.assertIsInstance(user, User)
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_user_attributes(self):
        """Test User attributes."""
        user = User()

        user.email = "test@example.com"
        user.password = "123456"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")                                                      
        self.assertEqual(user.password, "123456")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
