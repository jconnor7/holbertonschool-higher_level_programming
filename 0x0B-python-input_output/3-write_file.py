#!/usr/bin/python3
"""Write to a file """


def write_file(filename="", text=""):
    """Writes a string to a text file and returns
    the number of characters written.
    Args:
        filename: name of file being used
        text: text that will be written
    """
    with open(filename, mode="w", encoding="UTF8") as a_file:
        w2f = a_file.write(text)
        return (w2f)
