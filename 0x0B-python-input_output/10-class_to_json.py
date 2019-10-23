#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object
    Args:
        obj: object to change
    """
    return(obj.__dict__)
