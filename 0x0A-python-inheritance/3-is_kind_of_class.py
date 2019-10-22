#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Checks if the obj is an instance of or if the obj is
    an instance of a class that inherited from the specified class
    Args:
        obj: object
        a_class: class
    Return:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
