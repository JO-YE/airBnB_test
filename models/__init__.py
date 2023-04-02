#!/usr/bin/python3
from models.engine.file_storage import FileStorage
# Used the method of importing packages

storage = FileStorage()
storage.reload()
# the reload method from file storage and it deserializes
