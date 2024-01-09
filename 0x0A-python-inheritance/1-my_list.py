#!/usr/bin/python3
"""
This class inherits from the list class and includes a method to print the sorted list.
"""

class MyList(list):
    """
    MyList class inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Print the list in sorted order (ascending).

        :return: None
        """
        sorted_list = sorted(self)
        print(sorted_list)
