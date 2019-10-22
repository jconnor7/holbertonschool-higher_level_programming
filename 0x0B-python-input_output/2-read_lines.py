#!/usr/bin/python3
"""Read n lines"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file and prints it to stdout"""
    with open(filename, mode="r", encoding="UTF8") as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            for line in range(nb_lines):
                print(a_file.readline(), end="")
