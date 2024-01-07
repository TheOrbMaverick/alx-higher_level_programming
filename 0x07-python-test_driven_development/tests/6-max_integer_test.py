import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_basic(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_max_integer_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_integer_mixed_types(self):
        self.assertEqual(max_integer([1, 'a', 3, 2]), 3)

    def test_max_integer_single_value(self):
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_floats(self):
        self.assertEqual(max_integer([3.14, 2.71, 1.618]), 3.14)

if __name__ == '__main__':
    unittest.main()
