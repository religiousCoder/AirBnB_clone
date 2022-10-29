#!/usr/bin/python3
""" Stores objects in a file."""
import json
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
        dict_obj = {}

        for obj_id, obj_id_dict in self.__objects.items():
             dict_obj[obj_id] = {}
             for k, v in obj_id_dict.items():
                   if k == 'created_at' or k == 'updated_at':
                        dict_obj[obj_id][k] = datetime.fromisoformat(v)
                   else:
                        dict_obj[obj_id][k] = v
        return dict_obj

    def new(self, obj):
        """ Sets in `__objects` `obj.to_dict` with key `<obj class name>.id`.

            Args:
                obj: the object to set its dicts.
        """
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj.to_dict()

    def save(self):
        """  Serializes `__objects` to the JSON file `__file_path`.
        """
        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """ Deserializes the JSON file `__file_path` if it exists,
            otherwise does nothing.
        """
        try:
            with open(self.__file_path, 'r') as json_file:
                self.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
