#!/usr/bin/python3
""" Define a class Rectangle that inherits class BasGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Implements ... """
    def __init__(self, width, height):
        """ Implemantation """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
