import unittest


def factorial(num: int) -> int:
    """
    Return the factorial of the given number.
    """
    pass


# =========
#  TESTING
# =========
class FactorialTestCase(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(20), 2432902008176640000)


unittest.main()
