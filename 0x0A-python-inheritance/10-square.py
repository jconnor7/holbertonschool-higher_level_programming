#!/usr/bin/python3
"""Square #1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """initialize size using super to call the parent class attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
