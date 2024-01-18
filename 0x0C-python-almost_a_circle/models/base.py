#!/usr/bin/python3

"""
This module defines the Base class, which is inherited by other classes.
"""

import json

class Base:
    """
    The Base class is the base class for all other classes in this project.

    Attributes:
    __nb_objects (int): A private class attribute to manage the id attribute in all classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
        list_dictionaries (list): A list of dictionaries.

        Returns:
        str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
        list_objs (list): A list of instances that inherit from Base.

        Returns:
        None
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                list_objs = []
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
        json_string (str): A JSON string representing a list of dictionaries.

        Returns:
        list: A list represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
        **dictionary: A dictionary representing attribute-value pairs.

        Returns:
        Base: An instance with attributes set based on the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Creating a "dummy" Rectangle instance with mandatory attributes (width, height)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Creating a "dummy" Square instance with mandatory attribute (size)
        else:
            dummy_instance = cls()  # Creating a generic "dummy" instance

        dummy_instance.update(**dictionary)  # Updating the "dummy" instance with real values from the dictionary
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file and return a list of instances.

        Returns:
        list: A list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []


    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares using Turtle graphics.

        Args:
        list_rectangles (list): A list of Rectangle instances.
        list_squares (list): A list of Square instances.

        Returns:
        None
        """
        screen = turtle.Screen()
        screen.bgcolor("white")

        # Draw Rectangles
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")  # You can choose any color you like
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.end_fill()

        # Draw Squares
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")  # You can choose any color you like
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()

        turtle.exitonclick()
