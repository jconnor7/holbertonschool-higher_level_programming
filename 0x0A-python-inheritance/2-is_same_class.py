#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of the specified class
    Args:
        Obj: object
        a_class: class
    Return:
        True, if obj is exactly an instance
        False, if not
    """
    if type(obj) is a_class:
        return True
    else:
        return False
