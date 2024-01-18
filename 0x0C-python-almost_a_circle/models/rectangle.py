#!/usr/bin/python3

"""
This module defines the Rectangle class, which inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class inherits from the Base class
    and represents a rectangle.

    Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
    x (int): X-coordinate of the top-left corner of the rectangle.
    y (int): Y-coordinate of the top-left corner of the rectangle.
    id (int): Identifier of the rectangle.

    Methods:
    __init__(self, width, height, x=0, y=0, id=None):
        Constructor for the Rectangle class.
        - Calls the super class with id, utilizing the
        logic of the __init__ method of the Base class.
        - Assigns the provided arguments (width, height, x, y)
        to the corresponding attributes.
    area(self): Public method that returns the area
    value of the Rectangle instance.
    display(self): Public method that prints the Rectangle
    instance using the character,
    # taking into account x and y.
    __str__(self): Overridden method that returns a string
    representation of the Rectangle.
    update(self, *args, **kwargs): Public method that assigns no-keyword
    and keyword arguments to attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int, optional): X-coordinate of the top-left
        corner of the rectangle (default is 0).

        y (int, optional): Y-coordinate of the top-left
        corner of the rectangle (default is 0).
        id (int, optional): Identifier of the rectangle (default is None).
        """
        super().__init__(id)  # Calls the super class with id using the logic.
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        self._validate_integer("width", value)
        self._validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        self._validate_integer("height", value)
        self._validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x attribute."""
        self._validate_integer("x", value)
        self._validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y attribute."""
        self._validate_integer("y", value)
        self._validate_non_negative("y", value)
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance using the character #
        taking into account x and y."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle with the provided
        no-keyword and keyword arguments.

        Args:
        *args: No-keyword arguments in the order id, width, height, x, y.
        **kwargs: Keyword arguments representing attribute-value pairs.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def _validate_integer(self, attr_name, value):
        """Validate that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")

    def _validate_positive(self, attr_name, value):
        """Validate that the value is greater than 0."""
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def _validate_non_negative(self, attr_name, value):
        """Validate that the value is greater than or equal to 0."""
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle.

        Returns:
        dict: A dictionary containing attribute-value pairs.
        """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
