#!/usr/bin/python3
"""Class assign"""


class Square:
    """1 Attribute"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an intege")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
