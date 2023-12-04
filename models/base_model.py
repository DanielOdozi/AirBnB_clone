#!/usr/bin/python3
'''A class BaseModel'''
import uuid
import datetime


class BaseModel:
    """Class that defines properties of BaseModel.

     Attributes:
        id (int): Identity of each instance.
    """
    def __init__(self) -> None:
        """Creates new instances of Base.

        Args:
            id (int, optional): Identity of each instance.
        """
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def update(self):
        '''Update the time everytime object is called'''
        self.updated_at = datetime.datetime.now()

    def save(self):
        '''updates updated_at with the current datetime'''
        self.updated_at = datetime.datetime.now()

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
