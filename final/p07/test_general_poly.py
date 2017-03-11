import unittest
from general_poly import *

class GeneralPolyTest(unittest.TestCase):
    def test_it_can_evaluate_general_poly_function(self):
        L = [1, 2, 3, 4]
        x = 10
        expected = 1234
        actual = general_poly(L)(x)

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
