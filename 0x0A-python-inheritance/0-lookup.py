#!/usr/bin/python3
def lookup(obj):
    attributes_methods = []

    # Iterate through all attributes and methods of the object
    for attr_name in dir(obj):
        # Exclude built-in attributes and methods
        if not attr_name.startswith('__'):
            attributes_methods.append(attr_name)

    return attributes_methods
