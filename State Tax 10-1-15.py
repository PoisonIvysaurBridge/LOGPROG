'''
Write a program that will determine the additional state tax owed by an employee.
The state charges a 4% tax on net income.
Net income is determined by subtracting a PhP 3000.00 for each dependent on gross income.
Your program segment will read gross income, number of dependents,
and tax amount already deducted.
It will then compute the actual tax owed and print the difference between tax owed and
tax deductedfollowed by the message 'SEND CHECK' or 'REFUND' depending on whether this
difference is positive or negative

read: to get input from the user

'''

strInput=input('enter gross income: ')
gross= float(strInput)
strInput=input('enter number of dependents: ')
kids=int(strInput)
strInput=input('tax amount already deducted: ')
deducted=float(strInput)

netIncome= gross-3000*kids
tax=netIncome*0.04
actualTax= tax-deducted
print(actualTax)
if actualTax > 0:
    print('SEND CHECK')
elif actualTax < 0:
    print('REFUND')


