#!/usr/bin/python3
"""
Module documentation: append_after

This module contains a function to insert a line of text after each line
containing a specific string in a file.

"""

def append_after(filename="", search_string="", new_string=""):
    """
    Function documentation: append_after

    This function takes a filename, a search string, and a new string. It
    inserts the new string after each line in the file that contains the
    specified search string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing the
                          search string.

    """
    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
