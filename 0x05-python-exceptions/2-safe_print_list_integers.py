def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for item in my_list[:x]:
            if type(item) == int:
                print("{:d}".format(item), end=" ")
                count += 1
        print()  # New line after printing integers
    except (ValueError, TypeError):
        pass

    return count
