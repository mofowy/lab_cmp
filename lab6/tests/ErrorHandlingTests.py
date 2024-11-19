import unittest
from lab6.functions.calcFunctions import add, subtract, multiply, divide, power, sqrt, modulus

class TestErrorHandling(unittest.TestCase):

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add('string', 5)

if __name__ == '__main__':
    unittest.main()