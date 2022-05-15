#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dictionary = {}
        if cls:
            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    dictionary[key] = value
            return dictionary
        return FileStorage.__objects

    def delete(self, obj=None):
        """Deletes an object from storage"""
        if obj:
            for key, value in FileStorage.__objects.items():
                if value == obj:
                    del FileStorage.__objects[key]
                    self.save()
                    return
        else:
            pass

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        - only if the JSON file (__file_path) exists
        - otherwise, do nothing.
        - If the file doesn't exist, no exception should be raised."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                js = json.load(file)
                for key, value in js.items():
                    reloadobj = classes[js[key]['__class__']](**js[key])
                    self.__objects[key] = reloadobj
        except FileNotFoundError:
            pass

    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.reload()
