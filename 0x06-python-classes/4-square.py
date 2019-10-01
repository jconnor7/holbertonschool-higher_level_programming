#!/usr/bin/python3
class Square:
    """ Creates a class called square"""

    def __init__(self, size=0):
        """ Creates a private instance attribute, size
        Args:
            - size: size of square
        """
        self.__size = size

    def area(self):
        """ Finds the area of a square
        Returns:
            - Current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Sets the size of the square
        Args:
            - value(int): size of the square
        Raises:
            - TypeError: if the size is not an integer
            - ValueError: if size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value
