#!/usr/bin/python3
"""
This function takes an object as input and returns a list of its attributes and methods.
"""

def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    :param obj: The input object
    :return: List of strings representing attributes and methods
    """
    return [attr for attr in dir(obj) if callable(getattr(obj, attr)) or not attr.startswith("__")]
