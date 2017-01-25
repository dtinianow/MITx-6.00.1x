def remaining_balance(originalBalance, annualInterestRate, monthlyPaymentRate):
    balance = originalBalance

    for month in range(12):
        minimumPayment = balance * monthlyPaymentRate
        balance -= minimumPayment
        monthlyInterestRate = annualInterestRate / 12.0
        interest = monthlyInterestRate * balance
        balance += interest

    return 'Remaining balance: %s' % round(balance, 2)
