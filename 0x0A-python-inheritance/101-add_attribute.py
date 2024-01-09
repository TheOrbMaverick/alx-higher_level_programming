#!/usr/bin/python3
"""
This function adds a new attribute to an object if it's possible.
"""

def add_attribute(obj, attr, value):
    """
    Add a new attribute to the object if it's possible.

    :param obj: The object to which the attribute should be added
    :param attr: The attribute name
    :param value: The value for the attribute
    :raise: TypeError if the object can't have a new attribute
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    object.__setattr__(obj, attr, value)
