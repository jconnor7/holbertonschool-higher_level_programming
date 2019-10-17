#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """sort and print the list"""
        print(sorted(self))
