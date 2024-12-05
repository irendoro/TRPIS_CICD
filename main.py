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

def add_numbers(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

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

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 4), 7)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(3, -4), -1)

class TestIsPrime(unittest.TestCase):
    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_prime_number(self):
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_is_prime_non_prime(self):
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(4))

    def test_is_prime_large_prime(self):
        self.assertTrue(is_prime(7919))

if __name__ == "__main__":
    unittest.main()
