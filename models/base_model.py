#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

Base = declarative_base()


class BaseModel:
    """BASE MODEL TO BE DECLARED USING THE BASE MODEL

    Attributes:
        id (sqlalchemy String): THE IDENTIFICATION
        created_at (sqlalchemy DateTime): WHEN IT WAS CREATED AND ALL
        updated_at (sqlalchemy DateTime):LAST UPDATE TO BE CHECKED 
    """

    id = Column(String(60), primary_key=True, nullable=False)
    day_created = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_info = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Prototype of the base model in check

        Args:
            *args (any):not used in this context
            **kwargs (dict):pairs in the attributes in question
        """
        self.id = str(uuid4())
        self.day_created = self.updated_info = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "day_created" or key == "updated_info":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """information updated and finalised """
        self.updated_info = datetime.utcnow()
        models.new_storage.new(self)
        models.new_storage.save()

    def to_dict(self):
        """dictionary with information will be returned 
        """
        dictionary_mine = self.__dict__.copy()
        dictionary_mine["__class__"] = str(type(self).__name__)
        dictionary_mine["day_created"] = self.day_created.isoformat()
        dictionary_mine["updated_info"] = self.updated_info.isoformat()
        dictionary_mine.pop("_sa_instance_state", None)
        return dictionary_mine

    def delete(self):
        """delete the information from storage"""
        models.new_storage.delete(self)

    def __str__(self):
        """instance returned into prospect"""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
