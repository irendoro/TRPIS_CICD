import unittest

def factorial(n):
    """
    @brief Вычисляет факториал числа n.
    
    Эта функция принимает число n и возвращает его факториал (n!).
    Если число отрицательное, возбуждается исключение ValueError.
    
    @param n Целое число, для которого вычисляется факториал.
    @return Возвращает факториал числа n.
    @throws ValueError Если n < 0.
    
    @code
    factorial(5) -> 120
    factorial(0) -> 1
    @endcode
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def add_numbers(a, b):
    """
    Эта функция принимает два числа a и b, и возвращает их сумму.
    """
    return a + b

def is_prime(n):
    """
    @brief Проверяет, является ли число простым.
    
    Эта функция проверяет, является ли заданное число простым.
    
    @param n Целое число, которое проверяется на простоту.
    @return True, если число простое, иначе False.
    
    @code
    is_prime(2) -> True
    is_prime(9) -> False
    @endcode
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def multiply_numbers(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

class TestFactorial(unittest.TestCase):
    """
    @brief Тесты для функции factorial.
    
    Этот класс содержит тесты для проверки правильности работы функции factorial.
    """
    def test_factorial_zero(self):
        """
        @brief Проверяет факториал для нуля.
        """
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        """
        @brief Проверяет факториал для единицы.
        """
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        """
        @brief Проверяет факториал для положительных чисел.
        """
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_negative(self):
        """
        @brief Проверяет обработку ошибки для отрицательных чисел.
        """
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_large_factorial(self):
        """
        @brief Проверяет факториал для большого числа.
        """
        self.assertEqual(factorial(10), 3628800)

class TestAddNumbers(unittest.TestCase):
    """
    @brief Тесты для функции add_numbers.
    
    Этот класс содержит тесты для проверки правильности работы функции add_numbers.
    """
    
    def test_add_positive_numbers(self):
        """
        @brief Проверяет сложение двух положительных чисел.
        """
        self.assertEqual(add_numbers(3, 4), 7)

    def test_add_negative_numbers(self):
        """
        @brief Проверяет сложение двух отрицательных чисел.
        """
        self.assertEqual(add_numbers(-3, -5), -8)

    def test_add_mixed_numbers(self):
        """
        @brief Проверяет сложение одного положительного и одного отрицательного числа.
        """
        self.assertEqual(add_numbers(3, -4), -1)

class TestIsPrime(unittest.TestCase):
    """
    @brief Тесты для функции is_prime.
    
    Этот класс содержит тесты для проверки правильности работы функции is_prime.
    """
    
    def test_is_prime_zero(self):
        """
        @brief Проверяет, что 0 не является простым числом.
        """
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        """
        @brief Проверяет, что 1 не является простым числом.
        """
        self.assertFalse(is_prime(1))

    def test_is_prime_two(self):
        """
        @brief Проверяет, что 2 является простым числом.
        """
        self.assertTrue(is_prime(2))

    def test_is_prime_prime_number(self):
        """
        @brief Проверяет, что числа 11 и 13 являются простыми.
        """
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_is_prime_non_prime(self):
        """
        @brief Проверяет, что числа 9 и 4 не являются простыми.
        """
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(4))

    def test_is_prime_large_prime(self):
        """
        @brief Проверяет, что 7919 является простым числом.
        """
        self.assertTrue(is_prime(7919))

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_numbers(-3, -5), 15)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply_numbers(3, -4), -12)

if __name__ == "__main__":
    unittest.main()