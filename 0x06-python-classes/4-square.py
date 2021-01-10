#!/usr/bin/python3
"""Class assign"""


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
        """[Property to get size square]

        Returns:
            Square size.
        """
        return self.__size

    def area(self):
        """[Calcular area]

        Returns:
            [int]: [square area]
        """
        return self.__size*self.__size

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
