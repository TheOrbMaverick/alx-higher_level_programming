import unittest
import sys
import os

# Add the parent directory to the sys.path to access the 'models' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'models')))

from base import Base  # Import the Base class from models/base.py


class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):

        # Test the constructor when an id is provided
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_constructor_without_id(self):

        # Test the constructor when no id is provided
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

if __name__ == '__main__':
    unittest.main()
