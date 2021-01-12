#!/usr/bin/python3
"""Class asign"""


class Rectangle:
    """1 Atributte"""

    def __init__(self, width=0, height=0):
        """[Constructor]

        Args:
            Width: Default 0
            Height: Default 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (2 * (self.height + self.width)) == 0:
            return 0
        else:
            return (2 * (self.height + self.width))
