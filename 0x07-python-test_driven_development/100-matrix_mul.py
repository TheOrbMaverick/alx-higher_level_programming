#!/usr/bin/python3
"""
This function multiplies two matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    :param m_a: The first matrix (list of lists of integers or floats)
    :param m_b: The second matrix (list of lists of integers or floats)
    :return: The product of the matrices
    :raise: TypeError or ValueError with specific messages based on validation requirements
    """

    # Validate m_a
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a[1:]):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_b[0]) for row in m_b[1:]):
        raise TypeError("each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
