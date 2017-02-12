import unittest

from dict_interdiff import *

class DictInterdiffTest(unittest.TestCase):
    def test_it_can_find_intersections_and_differences_for_addition(self):
        d1 = {1:30, 2:20, 3:30, 5:80}
        d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
        actual = dict_interdiff(d1, d2)
        expected = ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

        self.assertEqual(actual, expected)

    def test_it_can_find_intersections_and_differences_for_greater_than(self):
        d1 = {1:30, 2:20, 3:30}
        d2 = {1:40, 2:50, 3:60}
        actual = dict_interdiff(d1, d2)
        expected = ({1: False, 2: False, 3: False}, {})

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
