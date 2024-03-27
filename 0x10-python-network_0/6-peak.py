#!/usr/bin/python3
"""
Module: find_peak
Contains a function to find a peak in a list of unsorted integers
"""

def find_peak(list_of_numbers):
    """Find a peak in a list of unsorted integers.

    Args:
        list_of_numbers (list): List of unsorted integers.

    Returns:
        int: A peak element from the list, if found.
             None if the list is empty.
    """

    if not list_of_numbers:
        return None
    
    low, high = 0, len(list_of_numbers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_numbers[mid] > list_of_numbers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    
    return list_of_numbers[low]

# Test the function
if __name__ == "__main__":
    test_list = [1, 2, 4, 6, 3]
    print(find_peak(test_list))
