#!/usr/bin/python3
"""Defines the FileStorage class."""

import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This Returns the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)

            from models.base_model import BaseModel

            for key, value in obj_dict.items():
                self.__objects[key] = BaseModel(**value)

        except FileNotFoundError:
            pass

