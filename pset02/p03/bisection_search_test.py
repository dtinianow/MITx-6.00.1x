import unittest

from bisection_search import fixed_monthly_payment

class BisectionSearchTest(unittest.TestCase):

    def test_it_can_calculate_fixed_payment_starting_with_320000(self):
        balance = 320000
        annualInterestRate = 0.2
        actual = fixed_monthly_payment(balance, annualInterestRate)
        expected = 'Lowest Payment: 29157.09'
        self.assertEqual(actual, expected)

    def test_it_can_calculate_fixed_payment_starting_with_999999(self):
        balance = 999999
        annualInterestRate = 0.18
        actual = fixed_monthly_payment(balance, annualInterestRate)
        expected = 'Lowest Payment: 90325.03'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
