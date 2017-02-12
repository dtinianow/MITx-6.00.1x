import unittest

from dot_product import *

class DotProductTest(unittest.TestCase):
    def test_it_can_calculate_the_sum_of_products_across_two_lists(self):
        listA = [1, 2, 3]
        listB = [4, 5, 6]
        actual = dotProduct(listA, listB)
        expected = 32

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
