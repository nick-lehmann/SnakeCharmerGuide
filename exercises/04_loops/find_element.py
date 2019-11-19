""" Find an element in a list. """
import unittest
from typing import List, Optional


def index_of(element: int, search_list: List[int]) -> Optional[int]:
    """
    Returns the index of the given element in `search_list`.

    If the element was not found, return None.
    """
    pass


# =========
#  TESTING
# =========
class IndexOfTestCase(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(index_of(2, [0, 1, 2, 3, 4, 5, 6, 7]), 2)
        self.assertEqual(index_of(3, [10, 45, 12, 98, 43, 3]), 5)
        self.assertEqual(index_of(4, [-3, -2, -1]), None)
        self.assertEqual(index_of(1, []), None)


unittest.main()
