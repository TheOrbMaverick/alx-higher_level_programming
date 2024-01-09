#!/usr/bin/python3
"""
Module documentation: json_file_loader

This module contains a function to load an object from a JSON file.

"""

import json

def load_from_json_file(filename):
    """
    Function documentation: load_from_json_file

    This function takes a filename as input, reads the JSON file, and returns
    the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python object loaded from the JSON file.

    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
