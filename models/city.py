#!/usr/bin/python3
"""
City class module, inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class defines attributes/methods for Cities:

    Public instance attributes:
    state_id (string): To contain id for a state, initialized with empty string
    name (string): To contain name of the state, initialized with empty string

    Magic method:
    __init__: Calls the __init__ method from parent with the super() method
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Class instantation: uses init from parent class wit super
        """
        super().__init__(*args, **kwargs)
