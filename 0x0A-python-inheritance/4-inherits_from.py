#!/usr/bin/python3
"""
This function checks if the object is an instance of a class that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The input object
    :param a_class: The specified class to check against
    :return: True if the object is an instance of a class that inherited from the specified class; otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
