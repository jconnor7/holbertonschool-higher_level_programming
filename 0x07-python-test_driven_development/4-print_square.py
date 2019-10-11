#!/usr/bin/python3
"""Print square
"""


def print_square(size):
    """Prints out a square with the character #
    Args:
        size: size of the square
    Raises:
        TypeError: raises error if size is not an int or
            if size is a float and less than 0
        ValueError: raises error if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
