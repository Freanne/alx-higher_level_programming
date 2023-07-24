#!/usr/bin/python3
""" Define a function that read files """


def read_file(filename=""):
    """ print output of file """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
