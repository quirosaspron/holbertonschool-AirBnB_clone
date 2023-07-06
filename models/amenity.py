#!/usr/bin/python3
"""
Amenity class module, inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class defines attributes/methods for Amenities:

    Public instance attributes:
    name (string): To contain Amenity name, initialized with empty string

    Magic method:
    __init__: Calls the __init__ method from parent with the super() method
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Class instantation: uses init from parent class wit super
        """
        super().__init__(*args, **kwargs)
