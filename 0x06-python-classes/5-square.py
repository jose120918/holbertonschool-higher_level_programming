#!/usr/bin/python3
"""Creación de clase"""


class Square:
    """1 Attribute"""

    def __init__(self, size=0):
        """[Constructor]

        Args:
            Size.
        """
        self.__size = size

    @property
    def size(self):
        """[Constructor]

        Args:
            Size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """[Constructor]

        Args:
            Size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """[Constructor]

        Args:
            Size.
        """
        return self.__size*self.__size

    def my_print(self):
        """[Constructor]

        Args:
            Size.
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
