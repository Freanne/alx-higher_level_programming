#!/bin/usr/bin/python3
""" A function that write in a file """


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
        """
    with open(filename, 'w', encoding='utf-8') as f:
        char_written = f.write(text)
        return char_written
