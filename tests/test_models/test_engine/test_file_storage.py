#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def test_create_instance(self):
        """Test creating FileStorage."""
        storage = FileStorage()


        self.assertIsInstance(storage, FileStorage)


    def test_all(self):
        """Test the all method."""
        storage = FileStorage()

        objects = storage.all()

        self.assertIsInstance(objects, dict)


if __name__ == "__main__":
    unittest.main()
