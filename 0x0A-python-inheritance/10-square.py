#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
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

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        :param width: The width of the rectangle
        :param height: The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        :return: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        :return: String representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        :param size: The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        :return: String representation of the square
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
