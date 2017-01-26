def fixed_monthly_payment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    lower = balance / 12
    upper = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

    while upper - lower > 0.01:
        fixedMonthlyPayment = (lower + upper) / 2
        currentBalance = balance

        for month in range(12):
            currentBalance -= fixedMonthlyPayment
            currentBalance += monthlyInterestRate * currentBalance

        if currentBalance < 0:
            upper = fixedMonthlyPayment
        else:
            lower = fixedMonthlyPayment

    return 'Lowest Payment: %s' % round(fixedMonthlyPayment, 2)
