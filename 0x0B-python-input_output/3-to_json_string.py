#!/usr/bin/python3
"""
Module documentation: json_converter

This module contains a function to convert an object (string) to its JSON
representation.

"""

import json

def to_json_string(my_obj):
    """
    Function documentation: to_json_string

    This function takes an object as input and returns its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the input object.

    """
    return json.dumps(my_obj)
