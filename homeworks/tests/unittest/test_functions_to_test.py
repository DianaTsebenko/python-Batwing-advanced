import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(12, 2), 14)
        self.assertEqual(Calculator.add(31, 69), 100)

    def test_substract(self):
        self.assertEqual(Calculator.subtract(276, 56), 220)
        self.assertEqual(Calculator.subtract(10, 0), 10)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(21, 3), 63)
        self.assertEqual(Calculator.multiply(109, 0), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(64, 64), 1)
        self.assertEqual(Calculator.divide(100, 50), 2)
        self.assertRaises(ValueError, Calculator.divide, 11, 0)

    if __name__ == '__main__':
        unittest.main()
