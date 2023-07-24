#!/usr/bin/python3
""" Define a checking-object function """


def is_kind_of_class(obj, a_class):
    """ implementation """

    if isinstance(obj, a_class):
        return True
    else:
        return False
