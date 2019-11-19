"""
Divide students into two teams.

There are some students standing in a row, each has some number
written on their back. The students are about to divide into two
teams by counting off by twos: those standing at the even positions
(0-based) will go to team A, and those standing at the odd position
will join the team B.

Your task is to calculate the difference between the sums of numbers
written on the backs of the students that will join team A, and those
written on the backs of the students that will join team B.

Task from CodeSignal:
https://app.codesignal.com/arcade/python-arcade/lurking-in-lists/xacqXRHoHhEC3dC4N
"""
import unittest
from typing import List, Optional


def divide_students(students: List[int]) -> int:
    """
    Divide the students as mentioned above and return
    the difference between the two teams.
    """
    pass


# =========
#  TESTING
# =========
class DivideStudentsTestCase(unittest.TestCase):
    def test_divide_tests(self):
        self.assertEqual(divide_students([1, 11, 13, 6, 14]), 11)
        self.assertEqual(divide_students([16, 14, 79, 8, 71, 72, 71, 10, 80, 76, 83, 70, 57, 29, 31]), 209)
        self.assertEqual(divide_students([3, 4]), -1)


unittest.main()

