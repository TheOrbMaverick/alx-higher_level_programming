import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_create_rectangle_with_valid_values(self):
        rectangle = Rectangle(2, 4, 1, 1, 5)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 5)

    def test_create_rectangle_with_default_values(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertNotEqual(rectangle.id, 0)  # Ensure id is automatically assigned

    def test_area_method(self):
        rectangle = Rectangle(3, 5)
        self.assertEqual(rectangle.area(), 15)

    def test_display_method(self):
        rectangle = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Add more test cases for other methods in the Rectangle class

if __name__ == '__main__':
    unittest.main()
