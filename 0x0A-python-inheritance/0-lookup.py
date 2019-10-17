#!/usr/bin/python3
"""Lookup"""


def lookup(obj):
    """A function that returns the list of available
    attributes and methods of an object
    Args:
        Obj
    Return:
        list of available attributes and methods
    """
    return (dir(obj))
