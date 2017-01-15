import unittest

from longest_alphabetic_substring import longest_alphabetic_substring

class LongestAlphabeticSubstringTest(unittest.TestCase):

    def test_it_can_find_the_longest_alphabetic_substring(self):
        s = 'azcbobobegghakl'
        actual = longest_alphabetic_substring(s)
        expected = "Longest substring in alphabetical order is: beggh"
        self.assertEqual(actual, expected)

    def test_it_should_return_first_match_in_a_tie(self):
        s = 'abcbcd'
        actual = longest_alphabetic_substring(s)
        expected = "Longest substring in alphabetical order is: abc"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
