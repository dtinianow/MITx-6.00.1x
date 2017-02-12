import unittest
from closest_power import *

class ClosestPowerTest(unittest.TestCase):
    def test_it_can_calculate_closest_power_of_3_to_12(self):
        actual = 2
        expected = closest_power(3,12)

        self.assertEqual(actual, expected)

    def test_it_can_calculate_closest_power_of_4_to_12(self):
        actual = 2
        expected = closest_power(4,12)

        self.assertEqual(actual, expected)

    def test_it_can_calculate_closest_power_of_4_to_1(self):
        actual = 0
        expected = closest_power(4,1)

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
