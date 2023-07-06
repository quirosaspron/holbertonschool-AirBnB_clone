#!/usr/bin/python3
"""
Place class module, inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class defines attributes/methods for Places:

    Public instance attributes:
    city_id (string): To contain city_id (from City class) where Place
    is located, initialized with empty string
    user_id (string): To contain user_id (from User class), initialized
    with empty string
    name (string): To contain Name of place, initialized with empty string
    desciption (string): To contain description of place, initialized
    with empty string
    number_rooms (integer): To contain the number of rooms that the place
    has, initialized with 0
    number_bathrooms (integer): To contain the number of bathrooms that
    the place has, initialized with 0
    max_guest (integer): To contain the maximum number of guests allowed
    in place, initialized with 0
    price_by_night (integer): To contain the price charged by night of stay
    in place, initialized with 0
    latitude (float): to contain the Latitude coordinate of place in
    decimal degrees units, initialized with 0.0
    longitude (float): to contain the Longitude coordinates of place in
    decial degrees units, initialized with 0.0
    amenity_ids (list of string): to contain a list of the amenities id's
    (from Ameniti class) that the place has, initialixed with empty string

    Magic method:
    __init__: Calls the __init__ method from parent with the super() method
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Class instantation: uses init from parent class wit super
        """
        super().__init__(*args, **kwargs)
