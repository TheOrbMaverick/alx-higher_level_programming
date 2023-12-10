#!/usr/bin/python3
def square_matrix_simple(matrix):
    # Create a new matrix with the square values
    squared_matrix = [[x**2 for x in row] for row in matrix]

    return squared_matrix
