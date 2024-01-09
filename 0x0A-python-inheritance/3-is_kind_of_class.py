#!/usr/bin/python3
"""
This function checks if the object is an instance of, or if it's an instance of a class that inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it's an instance of a class that inherited from, the specified class.

    :param obj: The input object
    :param a_class: The specified class to check against
    :return: True if the object is an instance of, or if it's an instance of a class that inherited from, the specified class; otherwise False
    """
    return isinstance(obj, a_class)
