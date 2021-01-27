#!/usr/bin/python3
'''Module for class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle, that inherits
    from: Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.error('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.error('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.error('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.error('y', value)
        self.__y = value

    @staticmethod
    def error(name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif (name == 'width' or name == 'hight') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == 'x' or name == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        return self.width*self.height

    def display(self):
        y_iterator = 0
        while (y_iterator < self.__y):
            print()
            y_iterator += 1
        for i in range(0, self.__height):
            x_iterator = 0
            while (x_iterator < self.__x):
                print(" ", end="")
                x_iterator += 1
            for j in range(0, self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        '''Update the class Rectangle attributes'''
        if len(args) > 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.__width = args[1]
                elif i == 2:
                    self.__height = args[2]
                elif i == 3:
                    self.__x = args[3]
                elif i == 4:
                    self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        '''Returns the dictionary representation
        of a Rectangle'''
        new_dict = {'id': self.id, 'width': self.__width,
                    'height': self.__height, 'x': self.__x, 'y': self.__y}
        return new_dict
