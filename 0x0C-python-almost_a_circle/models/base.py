#!/usr/bin/python3

class Base:
    """
    The Base class serves as a foundation for other classes in the project. It manages the 'id' attribute for instances
    and avoids duplicating code related to the 'id'.

    Attributes:
    __nb_objects (int): A private class attribute to keep track of the number of objects created.

    Methods:
    __init__(self, id=None): Constructor for the Base class.
        - If 'id' is provided, assigns it to the instance attribute 'id'.
        - If 'id' is not provided, increments __nb_objects and assigns the new value to 'id'.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
        id (int, optional): An integer representing the object's identifier. If provided, it is assigned to the 'id'
                           attribute. If not provided, __nb_objects is incremented, and the new value is assigned to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
