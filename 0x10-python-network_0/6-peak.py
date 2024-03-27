def find_peak(list_of_numbers):
    """Find a peak in a list of unsorted integers"""

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
