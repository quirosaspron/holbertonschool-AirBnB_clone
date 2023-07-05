#!/usr/bin/python3
""" serializes and deserializes instances from and to JSON file """
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return __objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        __objects[key] = obj

    def save(self):
        json_data = json.dumps(__objects)
        with open(self.__file_path, 'w') as file:
            file.write(json_data)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
