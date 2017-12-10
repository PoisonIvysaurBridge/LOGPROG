'''Practice 4
Write a program that will compute for the amount to be paid by a senior
citizen, given the total amount of food purchased. The amount entered is
VAT-inclusive. Senior citizens are exempted from VAT and are given 20%
discount on their food puchases.'''

strInput=input('Enter total amount: ')
AmountPaid=float(strInput)
OrigAmount=AmountPaid/1.12

LESSVAT=OrigAmount*0.12
LESSdis=OrigAmount*0.20

AmountDue=AmountPaid-LESSVAT-LESSdis

print('\nAmount          ',OrigAmount)
print('LESS VAT        ',-(LESSVAT))
print('LESS Discount   ',-(LESSdis))
print('======================')
print('Amount Due       ',AmountDue)
