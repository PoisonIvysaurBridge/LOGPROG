'''
12. Fast Food Chain
'''

print('Menu Choices')
print('Fried Chicken')
print('Burger Steak')
print('Tapsilog')

menu=input('enter menu choice: ')
order=input('enter order choice(Ala Carte/ Value Meal): ')

if menu=="Fried Chicken":
    if order=="Ala Carte":
        amount= 75
    else:
        amount= 85

elif menu=="Burger Steak":
    if order=="Ala Carte":
        amount= 40
    else:
        amount= 50

elif menu=="Burger Steak":
    if order=="Ala Carte":
        amount= 60
    else:
        amount= 70

strInput=input('enter age: ')
age=int(strInput)

if age >= 60:
    discount= 0.2*amount
    amount=amount-discount
    
print('amount due: ',amount)

strInput=input('Amount Paid: ')
amPaid=float(strInput)
change= amPaid-amount
print(change)

