#!/usr/bin/python3
"""
This function checks if the object is exactly an instance of the specified class.
"""

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    :param obj: The input object
    :param a_class: The specified class to compare against
    :return: True if the object is exactly an instance of the specified class; otherwise False
    """
    return type(obj) is a_class
