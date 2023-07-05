#!/usr/bin/python3
""" Defines a say_name function """


def say_my_name(first_name, last_name=""):
    """Prints a person's name.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
