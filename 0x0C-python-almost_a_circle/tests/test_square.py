import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_create_square_with_valid_values(self):
        square = Square(3, 2, 2, 7)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 7)

    def test_create_square_with_default_values(self):
        square = Square(3)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertNotEqual(square.id, 0)  # Ensure id is automatically assigned

    def test_area_method(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_display_method(self):
        square = Square(2)
        expected_output = "##\n##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Add more test cases for other methods in the Square class

if __name__ == '__main__':
    unittest.main()
