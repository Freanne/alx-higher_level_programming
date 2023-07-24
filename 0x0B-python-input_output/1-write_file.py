#!/bin/usr/bin/python3
""" A function that write in a file """


def write_file(filename="", text=""):
    """ return the number of characters written """
    with open(filename, 'w', encoding='utf-8') as file:
        char_written = file.write(text)
        return char_written
