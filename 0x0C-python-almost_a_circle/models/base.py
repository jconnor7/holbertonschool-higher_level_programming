#!/usr/bin/python3
"""Base class"""


class Base():
    """This is the base class that will be used for this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Assign the public instance attribute id
        to this argument value. Otherwise, increment
        __nb_objects and assign the new value to the
        public instance attribute id

        Args:
            id: value of self.id
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
