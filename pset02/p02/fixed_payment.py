def remaining_balance(balance, annualInterestRate):
    currentBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    fixedMonthlyPayment = 0

    while currentBalance > 0:
        currentBalance = balance
        fixedMonthlyPayment += 10

        for month in range(12):
            currentBalance -= fixedMonthlyPayment
            currentBalance += monthlyInterestRate * currentBalance


    return 'Lowest Payment: %s' % fixedMonthlyPayment
