import unittest

from count_bobs import count_bobs

class CountBobsTest(unittest.TestCase):

    def test_it_can_count_bobs(self):
        s = 'azcbobobegghakl'
        actual = count_bobs(s)
        expected = "Number of times bob occurs is: 2"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
