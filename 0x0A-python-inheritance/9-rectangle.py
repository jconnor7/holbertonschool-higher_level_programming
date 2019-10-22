#!/usr/bin/python3
"""Full rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ check width and height values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Description of the rectangle"""
        return ("[{}] {}/{}".format(type(self).__name__, self.__width,
                                    self.__height))
