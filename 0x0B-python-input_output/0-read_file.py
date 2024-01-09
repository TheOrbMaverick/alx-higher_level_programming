#!/usr/bin/python3
"""
Module documentation: read_file

This module contains a function to read a text file and print its contents to stdout.

"""

def read_file(filename=""):
    """
    Function documentation: read_file

    This function takes a filename as input, reads the content of the file,
    and prints it to the standard output.

    Args:
        filename (str): The name of the file to be read.

    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
