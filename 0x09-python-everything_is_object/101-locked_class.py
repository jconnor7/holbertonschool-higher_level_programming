#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """Creates a locked class that prevents user from
    dynamically creating new instance attributes,
    except if the new instance attribute is first_name"""
    __slots__ = ["first_name"]
