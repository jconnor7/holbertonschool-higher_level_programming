#!/usr/bin/python3
"""An addition module
add_integer: function that adds two integers together
"""


def add_integer(a, b=98):
    """Returns a + b
    Args: a and b (int): integers being added
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
