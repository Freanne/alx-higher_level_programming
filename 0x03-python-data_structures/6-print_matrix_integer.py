#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num enumerate(row):
            if i < len(matrix) - 1:
                print("{:d}".format(num), sep="")
            else:
                print("{:d}".format(num))
    if len(matrix) == 0:
        print()