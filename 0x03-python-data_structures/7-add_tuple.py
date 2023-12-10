def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two integers from each tuple (using 0 for missing values)
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)

    # Calculate the sum of corresponding elements
    result_tuple = (a[0] + b[0], a[1] + b[1])

    return result_tuple
