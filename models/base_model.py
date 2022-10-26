#!/usr/bin/python3
""" Base class for all other classes in the module.

"""
import uuid
from datetime import datetime

class BaseModel():
	
	def __init__(self):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now().isoformat()
		self.updated_at = datetime.now().isoformat()
	def __str__(self):
		return (f'[{type(self).__name__}] ({self.id}) \
{self.__dict__}')
	def save(self):
		self.updated_at = datetime.now().isoformat()
	def to_dict(self):
		instance_dict = self.__dict__
		instance_dict['__class__'] = f'{type(self).__name__}'
		return (instance_dict)

