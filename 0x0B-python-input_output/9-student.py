#!/usr/bin/python3
"""
Module documentation: student_class

This module defines a Student class with public attributes and a to_json method.

"""

class Student:
    """
    Class documentation: Student

    This class defines a student with public attributes: first_name, last_name,
    and age. It also has a method to retrieve a dictionary representation of a
    Student instance.

    """

    def __init__(self, first_name, last_name, age):
        """
        Method documentation: __init__

        This method initializes a Student instance with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method documentation: to_json

        This method retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.

        """
        # Get the dictionary representation of the object's attributes
        obj_dict = self.__dict__

        # Convert non-serializable attributes to serializable types
        serializable_dict = {}
        for key, value in obj_dict.items():
            if isinstance(value, (str, int)):
                serializable_dict[key] = value

        return serializable_dict
