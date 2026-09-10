#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class."""

    def test_create_instance(self):
        """Test creating a State."""
        state = State()

        self.assertIsInstance(state, State)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.name, str)

    def test_name(self):
        """Test the name attribute."""
        state = State()

        state.name = "California"

        self.assertEqual(state.name, "California")

if __name__ == "__main__":
    unittest.main()
