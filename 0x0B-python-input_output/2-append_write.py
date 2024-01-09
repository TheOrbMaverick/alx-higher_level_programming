#!/usr/bin/python3
"""
Module documentation: append_write

This module contains a function to append a string at the end of a text file
(UTF8) and returns the number of characters added.

"""

def append_write(filename="", text=""):
    """
    Function documentation: append_write

    This function takes a filename and a text string as input, appends the string
    to the end of the specified file (UTF8 encoded), and returns the number of
    characters added.

    If the file doesn't exist, it will be created.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The text string to be appended to the file.

    Returns:
        int: The number of characters added to the file.

    """
    with open(filename, 'a+', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    
    return num_chars_added
