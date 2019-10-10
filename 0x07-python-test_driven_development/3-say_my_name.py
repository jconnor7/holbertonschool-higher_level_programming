#!/usr/bin/python3
"""Say my name
"""


def say_my_name(first_name, last_name=""):
    """This function prints out My name is, followed by a first and a last name.
    Args:
        first_name: a first name.
        last_name: a last name.
    Raises:
        TypeError: raises an error if args aren't strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
