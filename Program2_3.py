'''
Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment(multiples of 10)
'''

monthlyPaymentRate = 0  # min fix amount should be paid per month
init_balance = balance  # save initial balance
monthlyInterestRate = annualInterestRate/12  # monthly int rate

while balance > 0:
    for i in range(12):
        '''
        new balance = current balance - ( monthly fix amount + (new_balance * interest rate) )
        '''
        balance = balance - monthlyPaymentRate + \
            ((balance - monthlyPaymentRate) * monthlyInterestRate)

    '''
    if balance is positive means bank is in loss, lent money is remaining, 
    previously calculated monthly payment is wrong
    and bank needs to take more money each month
    calculate new monthly payment again by increasing rs/$ 10
    do this unless balance goes to 0 or minus by the 12th month
    '''
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance

    '''
    1th month if balance is 0 or less means bank has 
    sucessfully recovered all the lent money
    '''
    if balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)
