'''
Exercise 3
Write a program that accept as input the sale amount and the age of the
customer and display the total amount to be paid. A 20% discount is
given to customers who are 60 and above.
S.
'''

strInput=input('enter sale amount: ')
sale=float(strInput)

strInput=input('enter age: ')
age=float(strInput)

if age>= 60:
    pay=sale-sale*0.2
    print(pay)

else:
    print(sale)
