#!/usr/bin/python3
class Square:
    """ Creates a class called square"""
    def __init__(self, size=0):
        """ Creates a private instance attribute, size(int)
        Args:
            - size: size of square
        Raises:
            - TypeError: must be an int
            - ValueError: must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
