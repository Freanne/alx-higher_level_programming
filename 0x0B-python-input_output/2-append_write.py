#!/usr/bin/python3
""" Define a function that append text to the file """


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        char_added = file.write(text)
        return char_added
