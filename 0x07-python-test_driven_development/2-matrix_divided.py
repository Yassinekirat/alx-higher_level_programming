#!/usr/bin/python3


def matrix_divided(matrix, div):
    """matrix divid"""

    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(message)

    row_length = len(matrix[0]) if matrix else 0

    new_matrix = []

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(message)
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
