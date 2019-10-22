#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
        filename = file that will be used
    """
    with open(filename, mode='r', encoding="UTF8") as a_file:
        print(a_file.read(), end="")
