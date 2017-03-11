import unittest
from convert_to_mandarin import *

class ConvertToMandarinTest(unittest.TestCase):
    def test_it_can_convert_36_to_mandarin(self):
        actual = 'san shi liu'
        expected = convert_to_mandarin('36')

        self.assertEqual(actual, expected)

    def test_it_can_convert_20_to_mandarin(self):
        actual = 'er shi'
        expected = convert_to_mandarin('20')

        self.assertEqual(actual, expected)

    def test_it_can_convert_16_to_mandarin(self):
        actual = 'shi liu'
        expected = convert_to_mandarin('16')

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
