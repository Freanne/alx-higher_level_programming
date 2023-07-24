#!/usr/bin/python3
"""Defines class square inherit Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ implements the class """
    def __init__(self, size):
        """ size(int) : must be private.
            size: must be positive number validate by integer validator
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ return area of square """
        return self.__size ** 2

    def __str__(self):
        """ represent print and str """
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__size) + "/" str(self.__size)
        return string
