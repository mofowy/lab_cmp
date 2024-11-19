import unittest
from lab6.functions.calcFunctions import SubtractOperation as divide

class TestDivision(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 2), 3)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, 2), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()