#!/usr/bin/python3
"""
FileStorage class module
"""
import json


class FileStorage:
    """
    Private class attributes:
     file_path (string): path to the JSON file (ex: file.json)
     objects (dictionary): empty at the start, but it will be updated by
     new() method to store all objects

    Public instance methods:
     all(): returns the private class attribute objects
     new(obj): update the private class attribute objects
     save(): serializes the private class attribute objects to a JSON file
     reload(): if the JSON file exists, deserializes the JSON file to the
     private class attribute objects
    """
    file_path = "file.json"
    objects = {}

    def all(self):
        """
        Returns private class attribute objects that stores all objects
        """
        return self.objects

    def new(self, obj):
        """
        Update the private class attribute objects that stores all objects

        Args:
         *obj (dictionary): object
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.objects[key] = obj

    def save(self):
        """
        Serializes private class attribute objects, that stores all objects,
        to a JSON file: objects -> JSON file.
        """
        dic = {key: value.to_dict() for key, value in self.objects.items()}
        with open(self.file_path, "w", encoding="UTF-8") as json_file:
            json.dump(dic, json_file)

    def reload(self):
        """
        If JSON file exists, deserializes the JSON file to private class
        attribute objects, that stores all objects: JSON file -> objects
        """
        try:
            with open(self.file_path, "r", encoding="UTF-8") as json_file:
                json_object = json.load(json_file)
                # json_object contains several objects (attributes_dict)
                for key, attributes_dict in json_object.items():
                    # Identify class
                    class_type = eval(attributes_dict["class__"])
                    # Create object
                    obj = class_type(**attributes_dict)
                    self.new(obj)
        except FileNotFoundError:
            pass
