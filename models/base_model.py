#!/usr/bin/python3
""" Base class for all other classes in the module."""

import uuid
from datetime import datetime


class BaseModel():
    """ Defines all common attributes/methods for other classes.

        Attributes:
            id (str): A unique id generated upon instance creation.
            created_at (:obj:`datetime`): Saves the current datetime
                when an instance is created.
            updated_at (:obj:`datetime`): Saves the current datetime
                when an instance is created/updated.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today().isoformat()
        self.updated_at = datetime.today().isoformat()

    def __str__(self):
        """ Returns the string representation of a `BaseModel` instance.

        """
        return (f'[{type(self).__name__}] ({self.id}) \
{self.__dict__}')

    def save(self):
        """ Updates public instance attribute `updated_at`
            with the current datetime.
        """
        self.updated_at = datetime.today().isoformat()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
            of `__dict__` of the instance
        """
        instance_dict = self.__dict__
        instance_dict['__class__'] = f'{type(self).__name__}'
        return (instance_dict)