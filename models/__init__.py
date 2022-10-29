#!/usr/bin/python3
""" Create a unique `FileStorage` instance.

    Attributes:
        all: Stores module `file_storage`
        storage: A unique instance of class `FileStorage`
"""
from models.engine import file_storage


all = [file_storage]
storage = file_storage.FileStorage()
storage.reload()
