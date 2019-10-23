#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """To JSON string
    Returns the JSON representation of an object (string)
    Args:
        my_obj: input object
    """
    return(json.dumps(my_obj))
