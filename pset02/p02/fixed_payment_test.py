import unittest

from fixed_payment import remaining_balance

class FixedPaymentTest(unittest.TestCase):

    def test_it_can_calculate_fixed_payment_starting_with_3329(self):
        balance = 3329
        annualInterestRate = 0.2
        actual = remaining_balance(3329, 0.2)
        expected = 'Lowest Payment: 310'
        self.assertEqual(actual, expected)

    def test_it_can_calculate_fixed_paymeLnt_starting_with_4773(self):
        balance = 4773
        annualInterestRate = 0.2
        actual = remaining_balance(4773, 0.2)
        expected = 'Lowest Payment: 440'
        self.assertEqual(actual, expected)

    def test_it_can_calculate_fixed_payment_starting_with_3926(self):
        balance = 3926
        annualInterestRate = 0.2
        actual = remaining_balance(3926, 0.2)
        expected = 'Lowest Payment: 360'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
