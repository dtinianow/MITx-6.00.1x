import unittest

from count_vowels import count_vowels

class CountVowelsTest(unittest.TestCase):

    def test_it_can_count_vowels(self):
        s = 'azcbobobegghakl'
        actual = count_vowels(s)
        expected = 'Number of vowels: 5'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
