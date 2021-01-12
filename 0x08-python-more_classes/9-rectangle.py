#!/usr/bin/python3
"""Class asign"""


class Rectangle:
    """ Defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """[Constructor]

        Args:
            Width: Default 0
            Height: Default 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if (self.height == 0) or (self.width == 0):
            return ""

        return (((str(self.print_symbol) * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return (rect_1)

        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)

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
        return self.__height * self.__width

    def perimeter(self):
        if (self.__height == 0) or (self.__width == 0):
            return 0
        else:
            return (2 * (self.__height + self.__width))
