#!/usr/bin/python3
""" Defines a matrux_divided function"""
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list of lists.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by `div`, rounded to 2 decimal places.

    Raises:
        TypeError: If the `matrix` is not a list of lists of integers/floats,
            or if `div` is not a number.
        TypeError: If the rows of the matrix do not have the same size.
        ZeroDivisionError: If `div` is equal to zero.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
