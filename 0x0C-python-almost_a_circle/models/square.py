#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class and represents a square.

    Attributes:
    size (int): Size of the square.
    x (int): X-coordinate of the top-left corner of the square.
    y (int): Y-coordinate of the top-left corner of the square.
    id (int): Identifier of the square.

    Methods:
    __init__(self, size, x=0, y=0, id=None): Constructor for the Square class.
        - Calls the super class with id, x, y, width, and height using the logic of the __init__ method of the Rectangle class.
        - Assigns the provided argument size to both width and height attributes.
    __str__(self): Overridden method that returns a string representation of the Square.
    size(self): Getter method for the size attribute.
    size(self, value): Setter method for the size attribute.
    update(self, *args, **kwargs): Public method that assigns no-keyword and keyword arguments to attributes.
    to_dictionary(self): Public method that returns the dictionary representation of the Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int): Size of the square.
        x (int, optional): X-coordinate of the top-left corner of the square (default is 0).
        y (int, optional): Y-coordinate of the top-left corner of the square (default is 0).
        id (int, optional): Identifier of the square (default is None).
        """
        super().__init__(size, size, x, y, id)  # Calls the super class with id, x, y, width, and height using the logic of the __init__ method of the Rectangle class

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self._validate_integer("size", value)
        self._validate_positive("size", value)
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.

        Returns:
        dict: A dictionary containing attribute-value pairs.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square with the provided no-keyword and keyword arguments.

        Args:
        *args: No-keyword arguments in the order id, size, x, y.
        **kwargs: Keyword arguments representing attribute-value pairs.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
