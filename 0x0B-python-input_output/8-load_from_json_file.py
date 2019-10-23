#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file
    Args:
        filename: file that is read from
    """
    with open(filename, mode="r") as a_file:
        return (json.load(a_file))
