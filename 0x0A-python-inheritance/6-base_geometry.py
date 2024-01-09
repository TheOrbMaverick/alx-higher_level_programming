#!/usr/bin/python3
"""
This class defines a base geometry class with an unimplemented area method.
"""

class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area method.
    """

    def area(self):
        """
        Raises an exception with the message "area() is not implemented".

        :raise: Exception with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
