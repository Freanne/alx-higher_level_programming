#!/usr/bin/python3
""" Define class Rectangle """


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialization of width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ string representation """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += "#" * self.__width
            rect_str += "\n"
        return rect_str[:-1]

    def __repr__(self):
        """ return a string representation """
        return "Rectangle({}, {})".format(self.__width, self.__height)
