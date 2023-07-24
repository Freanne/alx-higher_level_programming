#!/usr/bin/python3
""" A function that check if an object is specific class """


def is_same_class(obj, a_class):
    """ Implement a verification of the istance of an object """
    if type(obj) == a_class:
        return True
    else:
        return False
