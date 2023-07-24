#!/usr/bin/python3
""" Define a function that checked inherited class of an object """


def inherits_from(obj, a_class):
    """ Implementations """

    if issubclass(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
