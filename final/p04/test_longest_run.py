import unittest
from longest_run import *

class LongestRunTest(unittest.TestCase):
    def test_it_can_find_longest_run_of_long_list(self):
        L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
        actual = 26
        expected = longest_run(L)

        self.assertEqual(actual, expected)

    def test_it_can_find_longest_run_of_short_list(self):
        L = [5, 4, 10]
        actual = 9
        expected = longest_run(L)

        self.assertEqual(actual, expected)

    def test_it_can_find_longest_run_of_sorted_list(self):
        L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = 45

        expected = longest_run(L)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
