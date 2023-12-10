#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx, value in enumerate(row):
            if col_idx != 0:
                print(" ", end="")
            print("{:d}".format(value), end="")
        print()
