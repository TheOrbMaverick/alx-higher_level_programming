#!/usr/bin/python3

import math

'''
This class defines MagicClass

'''


class MagicClass:
    """
    This class emulates the behavior of the given bytecode.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Parameters:
            radius (int or float, optional): The radius of the circle. Default is 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
