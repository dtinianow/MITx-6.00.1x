import unittest

from flatten import flatten

class FlattenTest(unittest.TestCase):
    def test_it_can_flatten_a_list_of_lists(self):
        aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
        actual = flatten(aList)
        expected = [1,'a','cat',2,3,'dog',4,5]

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
