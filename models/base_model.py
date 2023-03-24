#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue;
                elif key == 'updated_at' or key == 'created_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
# used fromisoformat to convert from string object to datetime object
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4()) # universal unique id
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}" 

# .__dict__ maps attribute names to their value.
# it returns the instances name and value in a dic form
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
# isoformat returns the string representation of the object
        return dict_copy
