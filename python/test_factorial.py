import unittest
from main import calculate_factorial

class TestFactorial(unittest.TestCase):
    
    def test_factorial_zero(self):
        self.assertEqual(calculate_factorial(0), 1)
    
    def test_factorial_one(self):
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_factorial_positive(self):
        self.assertEqual(calculate_factorial(5), 120)
    
    def test_factorial_large_number(self):
        self.assertEqual(calculate_factorial(10), 3628800)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
    
    def test_factorial_non_integer(self):
        with self.assertRaises(TypeError):
            calculate_factorial(3.14)

if __name__ == '__main__':
    unittest.main()