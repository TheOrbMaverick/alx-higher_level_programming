#!/usr/bin/python3
"""
Module documentation: class_serializer

This module contains a function to convert an instance of a class to a
serializable dictionary.

"""

def class_to_json(obj):
    """
    Function documentation: class_to_json

    This function takes an instance of a class and returns a dictionary
    description suitable for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary description for JSON serialization.

    """
    # Get the dictionary representation of the object's attributes
    obj_dict = obj.__dict__

    # Convert non-serializable attributes to serializable types
    serializable_dict = {}
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
