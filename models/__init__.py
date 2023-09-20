#!/usr/bin/python3
"""
an object is created now now
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    new_storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    new_storage = FileStorage()
new_storage.reload()
