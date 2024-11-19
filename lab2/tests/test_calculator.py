import unittest
from functions.calcFunctions import add, subtract, multiply, divide, power, sqrt, modulus

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(4, 0), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()
