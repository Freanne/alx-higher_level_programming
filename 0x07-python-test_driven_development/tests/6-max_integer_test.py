#!/usr/bin/python3
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for the max_integer function.
    """

    def test_regular_list(self):
        """
        Test max_integer with a regular list of integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

    def test_empty_list(self):
        """
        Test max_integer with an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """
        Test max_integer with a list of negative numbers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)

    def test_duplicate_values(self):
        """
        Test max_integer with a list containing duplicate values.
        """
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)

    def test_floats(self):
        """
        Test max_integer with a list of floating-point numbers.
        """
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.2]), 4.2)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)
        self.assertEqual(max_integer([10.5, 20.8, 30.1, 40.7]), 40.7)


if __name__ == '__main__':
    unittest.main()
