#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

from 9-rectangle import Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        :param size: The size of the square
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        :return: String representation of the square
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
