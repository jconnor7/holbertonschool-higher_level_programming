#!/usr/bin/python3
class Square:
    """ Creates a class called square"""

    def __init__(self, size=0):
        """ Creates a private instance attribute, size
        Args:
            - size: size of square
        Raises:
            - TypeError: if the size is not an integer
            - ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Finds the area of a square
        Returns:
            - Area of the square
        """
        return self.__size * self.__size
