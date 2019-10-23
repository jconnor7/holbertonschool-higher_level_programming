#!/usr/bin/python3
import json


def from_json_string(my_str):
    """From JSON string to Object
    Returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: JSON string being used
    """
    return(json.loads(my_str))
