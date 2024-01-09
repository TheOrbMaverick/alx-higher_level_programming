#!/usr/bin/python3
"""
Module documentation: add_item_script

This script adds command line arguments to a Python list and saves the list to
a file in JSON format.

"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items_to_list_and_save(arguments):
    """
    Function documentation: add_items_to_list_and_save

    This function takes a list of arguments, adds them to a Python list, and
    saves the list to a file in JSON format.

    Args:
        arguments (list): The list of command line arguments.

    """
    try:
        # Load existing data from file
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If file doesn't exist, initialize with an empty list
        existing_data = []

    # Add new arguments to the list
    existing_data.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(existing_data, "add_item.json")
