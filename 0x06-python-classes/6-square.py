#!/usr/bin/python3
class Square:
    """ Creates a class called square"""

    def __init__(self, size=0, position=(0, 0)):

        """ Sets the size of the square
        Args:
            - size(int): size of the square
            - position(int, int): position of object when printed
        Raises:
            - TypeError: if the size is not an integer
            - ValueError: if size is less than zero
            - TypeError: if not a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    def area(self):
        """ Finds the area of a square
        Returns:
            - Current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints a square of a certain size at a position
        self.size:
            calls size from the getter
        note:
            if you have a setter and getter you don't need to interact
            with private so that you don't mess up the values
        """
        if self.__size == 0:
            print()
            return

        for y_space in range(self.__position[1]):
            print()

        for row in range(self.__size):
            for x_space in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print()

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

    @property
    def position(self):
        """Returns position of the square
        position.setter:
            resets the position of the square
        Args:
            value(int): size of the square
        Raises:
            TypeError: if not a tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) or len(value) == 2 or
                isinstance(value[0], int) or isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
