#!/usr/bin/python3
"""
Module documentation: json_parser

This module contains a function to parse a JSON string and return the
corresponding Python data structure.

"""

import json

def from_json_string(my_str):
    """
    Function documentation: from_json_string

    This function takes a JSON string as input and returns the corresponding
    Python data structure.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.

    """
    return json.loads(my_str)
