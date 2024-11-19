import unittest
from lab6.functions.calcFunctions import multiply

class TestMultiplication(unittest.TestCase):
    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()