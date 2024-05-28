import unittest
from log_lib import logger
from app.calculator_app import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """
    Test suite for basic arithmetic operations implemented in a calculator application.
    """

    def setUp(self):
        """Log the start of a test."""
        logger.debug(f"Starting test: {self._testMethodName}")

    def tearDown(self):
        """Log the completion of a test."""
        logger.debug(f"Test completed: {self._testMethodName}")

    def test_add(self):
        """
        Test the addition function with positive, negative, and zero summands.
        """
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """
        Test the subtraction function with positive, negative, and zero results.
        """
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        """
        Test the multiplication function with positive, negative, zero, and mixed sign factors.
        """
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        """
        Test the division function including edge cases like division by zero.
        Note: Division by zero is expected to return 'inf' as per function definition in calculator_app.
        """
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(5, 0), 'inf')  # Testing division by zero


if __name__ == '__main__':
    unittest.main()
