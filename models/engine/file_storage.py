#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    # Used .to_dict to convert updated and created at from datetime to a string
    # using isoformat. it will also return the class__name__
    # So since we already did that in base.model module, we called it.
    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            d = {key : value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o['__class__']
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
