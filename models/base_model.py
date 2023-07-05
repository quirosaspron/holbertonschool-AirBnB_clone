#!/usr/bin/python3
""" BaseModel module """
import uuid
from datetime import datetime


class BaseModel():
    """ The base for the other classes """
    def __init__(self):
        """ Initializer method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.name = self.__class__.__name__

    def __str__(self):
        """ This will display some text """
        return("[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__))

    def save(self):
        """ Updates the time when modified """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary with the attributes of the class """
        dictionary = self.__dict__
        dictionary['__class__'] = self.name
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
