""" Calculate the fibonacci numbers. """
import unittest


def fibonacci(num: int) -> int:
    """
    Return the fibonacci number with index `num`.

    The first fibonacci number should have index 0.
    A fibonacci number is the sum of its two predecessors. The
    first two fibonacci numbers are 0 and 1.
    """
    pass


# =========
#  TESTING
# =========
class FibonacciTestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(20), 6765)


unittest.main()
