#!/usr/bin/python3
"""
This module defines a MyInt class that inherits from int with inverted == and != operators.
"""

class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equality operator.

        :param other: The object to compare with
        :return: True if self is not equal to other; otherwise, False
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator.

        :param other: The object to compare with
        :return: True if self is equal to other; otherwise, False
        """
        return super().__eq__(other)
