import unittest
from lab6.functions.calcFunctions import subtract

class TestSubtraction(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(-3, 2), -5)

if __name__ == '__main__':
    unittest.main()