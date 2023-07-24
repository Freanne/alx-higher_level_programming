#!/usr/bin/python3
""" Define class BaseGeometry """


class BaseGeometry:
    """ Implementation ... """
    def area(self):
        """ Raise an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} is not an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
