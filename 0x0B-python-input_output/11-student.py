#!/usr/bin/python3
"""
Module documentation: student_class

This module defines a Student class with public attributes and methods for
serialization and deserialization.

"""

class Student:
    """
    Class documentation: Student

    This class defines a student with public attributes: first_name, last_name,
    and age. It also has methods for retrieving a dictionary representation
    and replacing attributes based on a given dictionary.

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

    def to_json(self, attrs=None):
        """
        Method documentation: to_json

        This method retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing the attributes to be
                          included in the dictionary. If None, all attributes
                          will be included.

        Returns:
            dict: A dictionary representation of the Student instance.

        """
        # Get the dictionary representation of the object's attributes
        obj_dict = self.__dict__

        if attrs is None:
            return obj_dict

        # Filter attributes based on the provided list
        filtered_dict = {key: value for key, value in obj_dict.items() if key in attrs}
        return filtered_dict

    def reload_from_json(self, json):
        """
        Method documentation: reload_from_json

        This method replaces all attributes of the Student instance based on
        the provided dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names and values
                         are the new values for the attributes.

        """
        for key, value in json.items():
            setattr(self, key, value)
