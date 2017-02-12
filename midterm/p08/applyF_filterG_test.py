import unittest

from applyF_filterG import applyF_filterG

class ApplyFFilterGTest(unittest.TestCase):
    def test_it_can_mutate_a_list_and_return_the_largest_element(self):
        def f(i):
            return i + 2
        def g(i):
            return i > 5

        L = [0, -10, 5, 6, -4]
        largest = applyF_filterG(L, f, g)

        self.assertEqual(largest, 6)
        self.assertEqual(L, [5, 6])

    def test_it_returns_negative_one_if_list_is_empty(self):
        def f(i):
            return i + 2
        def g(i):
            return i > 5

        L = [0, -4]
        largest = applyF_filterG(L, f, g)

        self.assertEqual(largest, -1)
        self.assertEqual(L, [])

if __name__ == "__main__":
    unittest.main()
