import unittest

def factorial(n):
    """Вычисляет факториал числа n."""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_large_factorial(self):
        self.assertEqual(factorial(10), 3628800)

if __name__ == "__main__":
    unittest.main()
