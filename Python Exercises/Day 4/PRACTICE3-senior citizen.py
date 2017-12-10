'''Practice 3
Write a program that will compute for the amount to be paid by a senior
citizen, given the total amount of food purchased. Assume that the total
amount entered is before VAT. Senior citizens are exempted from VAT and
are given 20% discount on their food puchases.'''

amount=input('Enter total amount before VAT: ')
Sale=float(amount)

Discount=0.20
Deducted=Sale*Discount
AmountDue=Sale-Deducted

print('\nSale            ',Sale,'\n'+'Discount        ',-Deducted,'\n'+'======================\n'+'Amount Due       ',AmountDue)
