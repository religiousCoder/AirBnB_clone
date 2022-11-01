#!/usr/bin/python3
""" Stores objects in a file."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ Serializes intances to a JSON file and
        deserializes JSON file to instances.
    """
    #: str: Path to the Json file.
    __file_path = 'file.json'
    #: dict: Stores all objects by `<class name>.id`
    __objects = {}

    def all(self):
        """ Returns a dictionary of python objects in `__objects`.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in `__objects` `obj.to_dict` with key `<obj class name>.id`.

            Args:
                obj: the object to set its dicts.
        """
        FileStorage.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """  Serializes `__objects` to the JSON file `__file_path`.
        """
        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump({k: v.to_dict()
                      for k, v in FileStorage.__objects.items()}, json_file)

    def reload(self):
        """ Deserializes the JSON file `__file_path` if it exists,
            otherwise does nothing.
        """
        objects_dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                        'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as json_file:
            json_to_python_obj = None
            try:
                json_to_python_obj = json.load(json_file)
            except json.JSONDecodeError:
                pass
            if json_to_python_obj is None:
                return

            FileStorage.__objects = {key: objects_dict[key.split('.')[0]](**value)
                                     for key, value in json_to_python_obj.items()}
