""" Transform ugly lists into beautiful ones. """
import unittest
from typing import List


def beautify(ugly_list: List[int]) -> List[int]:
    """
    Transforms a ugly list into a beautiful one.

    Here, a list is considered beautiful if the first and the last element
    matches. To beautify a list, chop of its first and last element and check
    if became beautiful. If yeas, return this list. If not, continue chopping of.
    """
    pass

# =========
#  TESTING
# =========
class BeautifulListTestCase(unittest.TestCase):
    def test_beautify(self):
        self.assertEqual(
            beautify([3, 4, 2, 4, 38, 4, 5, 3, 2]),
            [4, 38, 4]
        )
        self.assertEqual(
            beautify([1, 4, -5]),
            [4]
        )
        self.assertEqual(
            beautify([]),
            []
        )
        self.assertEqual(
            beautify([1]),
            [1]
        )
        self.assertEqual(
            beautify([8, 5, 1, 2, 3, 8, 1, 10, 5, 1, 4, 6, 9, 2, 8, 8, 9, 4, 10, 3]),
            [8, 1, 10, 5, 1, 4, 6, 9, 2, 8]
        )


unittest.main()
