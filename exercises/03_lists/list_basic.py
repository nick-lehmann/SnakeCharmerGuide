""" Practice basic list operations. """
import unittest
from typing import List


def list_ends(input_list: List[int]) -> List[int]:
    """
    Return a list that just contains the first and the last element
    of the given list.
    """
    pass


def find_elements_less_than_10(input_list: List[int]) -> List[int]:
    """
    Return a list of all elements in input_list which are less than ten.
    """
    pass


# =========
#  TESTING
# =========
class BasicListTestCase(unittest.TestCase):
    def test_list_ends(self):
        self.assertEqual(
            list_ends([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            [1, 9]
        )
        self.assertEqual(
            list_ends([9, 8, 7, 6, 5, 4, 3, 2, 1]),
            [9, 1]
        )
        self.assertEqual(
            list_ends([1, 9]),
            [1, 9]
        )
        self.assertEqual(
            list_ends([1]),
            [1, 1]
        )

    def test_find_elements_less_than_10(self):
        self.assertEqual(
            find_elements_less_than_10([1, 2, 3, 13, 9, 12, 8]),
            [1, 2, 3, 9, 8]
        )
        self.assertEqual(
            find_elements_less_than_10([1, 2, 3, 4, 5, 6, 7]),
            [1, 2, 3, 4, 5, 6, 7]
        )
        self.assertEqual(
            find_elements_less_than_10([]),
            []
        )
        self.assertEqual(
            find_elements_less_than_10([10, 10, 10]),
            []
        )


unittest.main()
