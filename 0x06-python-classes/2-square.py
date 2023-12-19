#!/usr/bin/python3

"""
    This class defines a square.

    Attributes:
        __size (int): The size of the square.

    Initializes a new instance of the Square class.

    Parameters:
        size (int, optional): The size of the square. Default is 0.

"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int, optional): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
