#!/usr/bin/python3
"""Area and Perimeter of a Rectangle"""


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """Creates instance with attributes width and height
        Args:
            width: width of the rectangle
            height: height of a rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Finds the area of a rectangle
        Returns:
            Current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Finds the perimeter of a rectangle
        Returns:
           Current rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @property
    def width(self):
        """Sets the width of the rectangle
      Args:
          value(int): width of the square
      Raises:
          TypeError: if the width is not an integer
          ValueError: if width is less than zero
      """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Sets the height of the rectangle
        Args:
            value(int): height of the square
        Raises:
            TypeError: if the height is not an integer
            ValueError: if height is less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
