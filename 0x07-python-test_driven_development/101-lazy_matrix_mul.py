import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    :param m_a: The first matrix (list of lists of integers or floats)
    :param m_b: The second matrix (list of lists of integers or floats)
    :return: The product of the matrices
    :raise: ValueError with specific messages based on validation requirements
    """

    try:
        np_m_a = np.array(m_a, dtype=np.float64)
        np_m_b = np.array(m_b, dtype=np.float64)
        result = np.dot(np_m_a, np_m_b)
        return result.tolist()
    except (ValueError, TypeError) as e:
        raise ValueError(f"{e}: {type(e).__name__}") from None
