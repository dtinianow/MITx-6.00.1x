import unittest
from convert_to_mandarin import *

class ConvertToMandarinTest(unittest.TestCase):
    def test_it_can_convert_36_to_mandarin(self):
        actual = convert_to_mandarin('36')
        expected = 'san shi liu'

        self.assertEqual(actual, expected)

    def test_it_can_convert_20_to_mandarin(self):
        actual = convert_to_mandarin('20')
        expected = 'er shi'

        self.assertEqual(actual, expected)

    def test_it_can_convert_16_to_mandarin(self):
        actual = convert_to_mandarin('16')
        expected = 'shi liu'

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
