#!/usr/bin/python3
"""
Module documentation: json_file_saver

This module contains a function to save an object to a text file using its JSON
representation.

"""

import json

def save_to_json_file(my_obj, filename):
    """
    Function documentation: save_to_json_file

    This function takes an object and a filename as input, converts the object
    to its JSON representation, and writes it to the specified text file.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file to save the JSON representation.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False)
