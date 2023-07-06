#!/usr/bin/python3
"""
State class module, inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class defines attributes/methods for States:

    Public instance attributes:
    name (string): To contain name of state, initialized with empty string

    Magic method:
    __init__: Calls the __init__ method from parent with the super() method
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Class instantation: uses init from parent class wit super
        """
        super().__init__(*args, **kwargs)
