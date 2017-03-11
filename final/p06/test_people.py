import unittest
from people import *

class PeopleTest(unittest.TestCase):
    def test_people_can_return_specific_responses(self):
        e = Person('eric')
        le = Lecturer('eric')
        pe = Professor('eric')
        pe2 = Professor2('eric')
        ae1 = ArrogantProfessor1('eric')
        ae2 = ArrogantProfessor2('eric')

        actual = e.say('the sky is blue')
        expected = 'eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = le.say('the sky is blue')
        expected = 'eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = le.lecture('the sky is blue')
        expected = 'I believe that eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = pe.say('the sky is blue')
        expected = 'eric says: I believe that eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = pe.lecture('the sky is blue')
        expected = 'I believe that eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = ae1.say('the sky is blue')
        expected = 'eric says: It is obvious that eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = ae1.lecture('the sky is blue')
        expected = 'It is obvious that eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = ae2.say('the sky is blue')
        expected = 'eric says: It is obvious that I believe that eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = ae2.lecture('the sky is blue')
        expected = 'It is obvious that I believe that eric says: the sky is blue'

        self.assertEqual(actual, expected)

        actual = pe2.say('the sky is blue')
        expected = 'Prof. eric says: I believe that eric says: the sky is blue'

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
