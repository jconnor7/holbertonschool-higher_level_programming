#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Writes a string to a text file and returns
    the number of characters written.
    Args:
        filename: name of file being used
        text: text that will be written
    """
    with open(filename, mode="a", encoding="UTF8") as a_file:
        a2f = a_file.write(text)
        return (a2f)
