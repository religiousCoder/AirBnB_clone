#!/usr/bin/python3
""" Stores objects in a file."""
import json
import os
from datetime import datetime


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
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, json_file)

    def reload(self):
        """ Deserializes the JSON file `__file_path` if it exists,
            otherwise does nothing.
        """

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
            
            dict_obj = {}

            for obj_id, obj_id_dict in json_to_python_obj.items():
                dict_obj[obj_id] = {}
                for k, v in obj_id_dict.items():
                    if k == 'created_at' or k == 'updated_at':
                            dict_obj[obj_id][k] = datetime.fromisoformat(v)
                    else:
                            dict_obj[obj_id][k] = v
            FileStorage.__objects = dict_obj
            return FileStorage.__objects