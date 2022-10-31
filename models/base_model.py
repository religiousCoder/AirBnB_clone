#!/usr/bin/python3
""" Base class for all other classes in the module."""

import uuid
from datetime import datetime
import models


class BaseModel():
    """ Defines all common attributes/methods for other classes.

        Attributes:
            id (str): A unique id generated upon instance creation.
            created_at (:obj:`datetime`): Saves the current datetime
                when an instance is created.
            updated_at (:obj:`datetime`): Saves the current datetime
                when an instance is created/updated.
    """

    def __init__(self, *args, **kwargs):
        """ Initializes each instance of the class.

            Args:
                *args: Not used
                **kwargs: A keyword arguments constructor of a BaseModel.
        """
        if len(kwargs):
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        v_to_datetime = datetime.fromisoformat(v)
                        setattr(self, k, v_to_datetime)
                    else:
                        setattr(self, k, v)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """ Returns the string representation of a `BaseModel` instance.

        """
        return (f'[{type(self).__name__}] ({self.id}) \
{self.__dict__}')

    def save(self):
        """ Updates public instance attribute `updated_at`
            with the current datetime and serializes objects
            to a JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
            of `__dict__` of the instance
        """
        instance_dict = {k: v if type(v) not in [datetime]
                         else v.isoformat() for k, v in self.__dict__.items()}
        instance_dict['__class__'] = f'{type(self).__name__}'
        return (instance_dict)
