#!/usr/bin/python3

def no_c(my_string):
    # Create a new string without 'c' and 'C'
    new_string = ''.join(char for char in my_string if char.lower() not in ('c', 'C'))
    return new_string
