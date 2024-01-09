#!/usr/bin/python3
"""
Module documentation: write_file

This module contains a function to write a string to a text file (UTF8) and
returns the number of characters written.

"""

def write_file(filename="", text=""):
    """
    Function documentation: write_file

    This function takes a filename and a text string as input, writes the
    string to the specified file (UTF8 encoded), and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text string to be written to the file.

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    
    return num_chars_written
