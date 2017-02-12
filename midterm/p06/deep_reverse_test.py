import unittest

from deep_reverse import deep_reverse

class DeepReverseTest(unittest.TestCase):
    def test_it_can_deep_reverse_a_list_of_lists(self):
        L = [[1, 2], [3, 4], [5, 6, 7]]
        actual = deep_reverse(L)
        expected = [[7, 6, 5], [4, 3], [2, 1]]

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
