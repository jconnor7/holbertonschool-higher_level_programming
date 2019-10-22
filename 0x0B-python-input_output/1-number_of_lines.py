#!/usr/bin/python3
"""Number of lines """


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""
    line_count = 0
    with open(filename) as a_file:
        for line in a_file:
            line_count += 1
    return line_count
