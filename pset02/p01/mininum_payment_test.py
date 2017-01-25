import unittest

from mininum_payment import remaining_balance

class MinimumPaymentTest(unittest.TestCase):

    def test_it_can_calculate_remaining_large_balance(self):
        balance = 484
        annualInterestRate = 0.2
        monthlyPaymentRate = 0.04
        actual = remaining_balance(484, 0.2, 0.04)
        expected = 'Remaining balance: 361.61'
        self.assertEqual(actual, expected)

    def test_it_can_calculate_remaining_small_balance(self):
        balance = 42
        annualInterestRate = 0.2
        monthlyPaymentRate = 0.04
        actual = remaining_balance(42, 0.2, 0.04)
        expected = 'Remaining balance: 31.38'
        self.assertEqual(actual, expected)




if __name__ == "__main__":
    unittest.main()
