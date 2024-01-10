#!/usr/bin/python3
"""
This class defines a base geometry class with an unimplemented area method and an integer validator method.
"""

class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area method and an integer validator method.
    """

    def area(self):
        """
        Raises an exception with the message "area() is not implemented".

        :raise: Exception with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value.

        :param name: The name of the value
        :param value: The value to be validated
        :raise: TypeError if value is not an integer
                ValueError if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
