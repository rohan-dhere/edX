'''
Using Bisection Search to Make the Program Faster
'''


monthlyInterestRate = annualInterestRate/12  # monthly int rate
'''
min fix amount should be paid per month
assuming interest rate is 0
lower bound
'''
min_monthlyPaymentRate = balance/12

'''
max fix amount should be paid per month
assuming interest rate is applied at the end of 12 months,
not monthly
every month compound interest is added to current balance 
upper bound
'''
new_bal = balance
for x in range(0, 12):
    # add compound interest of 12 months
    new_bal = new_bal + (new_bal * monthlyInterestRate)

max_monthlyPaymentRate = new_bal/12  # upper bound

# mid value of upper and lower bound
monthlyPaymentRate = (min_monthlyPaymentRate + max_monthlyPaymentRate) / 2
init_balance = balance  # save initial balance

# 0.1 because 0 != 0.00012 so use a smaller float value
while abs(balance) > 0.1:
    # new mid value of upper and lower bound
    monthlyPaymentRate = (min_monthlyPaymentRate + max_monthlyPaymentRate)/2
    balance = init_balance  # wrong calculation start again
    for i in range(0, 12):
        balance = balance - monthlyPaymentRate + \
            ((balance - monthlyPaymentRate) * monthlyInterestRate)

    if balance > 0:  # if balance is ramaining at the 12th month then need to increase payment per month
        min_monthlyPaymentRate = monthlyPaymentRate

    elif balance < 0:  # if balance is negative at the 12th month then need to lower payment per month
        max_monthlyPaymentRate = monthlyPaymentRate

    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))  # print upto 2 decimals
