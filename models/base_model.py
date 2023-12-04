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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def update(self):
        '''Update the time everytime object is called'''
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        '''Return or print the classname'''
        return ("[{}] ({}) {}").format(self.__class__.__name__,
                                        self.id,
                                                self.__dict__)
