#!/usr/bin/python3
import json

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f'{self.__class__.__name__}.{self.id}'
        self.__objects[key] = obj

    # Used .to_dict to convert updated and created at from datetime to a string
    # using isoformat
    # So since we already did that in base.model module, we called it.
    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            d = {key : value.to_dict for key, value in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                obj_dict = json.load(f)
                obj_dict = eval(self.__class__.name__(obj_dict))
        except:
            pass
