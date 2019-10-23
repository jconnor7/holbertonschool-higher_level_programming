#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object that will be written to a text file
        filename: file that it will be written to
    """
    with open(filename, mode="w") as a_file:
        json.dump(my_obj, a_file)
