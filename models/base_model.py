#!/usr/bin/python3
'''A class BaseModel'''
import uuid
import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    """Class that defines properties of BaseModel.

     Attributes:
        id (int): Identity of each instance.
    """
    storage = FileStorage()

    def __init__(self, *args, **kwargs) -> None:
        """Creates new instances of Base.

        Args:
            id (int, optional): Identity of each instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.storage.new(self)

    def update(self):
        '''Update the time everytime object is called'''
        self.updated_at = datetime.datetime.now()

    def save(self):
        '''updates updated_at with the current datetime'''
        self.updated_at = datetime.datetime.now()

    def save(self):
        '''Call save(self) method of storage'''
        self.storage.save()

    def __str__(self):
        '''Return or print the classname'''
        return ("[{}] ({}) {}").format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__'''
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()

        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = created_at_iso
        obj_dict['updated_at'] = updated_at_iso

        return obj_dict
