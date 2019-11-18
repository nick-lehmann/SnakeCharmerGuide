import sys
import unittest


def century_from_year(year):
    """
    Return the century of the given year.
    """
    pass


# =========
#  TESTING
# =========
class CenturyTestCase(unittest.TestCase):
    def test_century(self):
        self.assertEqual(century_from_year(1905), 20)
        self.assertEqual(century_from_year(1700), 17)
        self.assertEqual(century_from_year(8), 1)
        self.assertEqual(century_from_year(200), 2)
        self.assertEqual(century_from_year(350), 4)


unittest.main()
