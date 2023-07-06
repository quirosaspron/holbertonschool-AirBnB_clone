#!/usr/bin/python3
"""
User class module, inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class defines attributes/methods for Users:

    Public instance attributes:
    email (string): To contain email adress, initialized with empty string
    password (string): To contain password, initialized with empty string
    first_name (string): To contain First Name, initialized with empty string
    Last Name (string): To contain Last Name, initialized with empty string

    Magic method:
    __init__: Calls the __init__ method from parent with the super() method
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Class instantation: uses init from parent class wit super
        """
        super().__init__(*args, **kwargs)
