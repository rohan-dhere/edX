'''
program to calculate the credit card balance after 
one year if a person only pays the minimum monthly 
payment required by the credit card company each month.
'''

'''
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
for x in range(12):
    # current bal =  total balance - Updated balance of each month
    balance = balance - (balance * monthlyPaymentRate) + ((balance -
                                                           (balance * monthlyPaymentRate)) * (annualInterestRate/12))
print("Remaining balance:", round(balance, 2))
