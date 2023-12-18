def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    try:
        for i in range(x):
            print(my_list[i], end=' ')
            elements_printed += 1
    except IndexError:
        pass  # Handle the exception if the index is out of range

    print()  # Print a newline after the elements
    return elements_printed
