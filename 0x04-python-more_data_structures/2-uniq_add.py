#!/usr/bin/python3
def uniq_add(my_list):
    # Use a set to store unique integers
    unique_integers = set(my_list)

    # Sum up the unique integers
    result = sum(unique_integers)

    return result
