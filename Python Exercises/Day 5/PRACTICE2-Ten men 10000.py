'''Practice 2
Ten young men agreed to purchase a gift worth 10,000 for their boss. In
addition, they agreed to continue their plan even if at least one of them
dropped out. Write a program that would input the number of men who
dropped out (assume 0 to 9 only) and output how much more will each
have to contribute toward the purchase of the gift.'''

strInput=input('Enter number of persons who dropped out: ')
drop=int(strInput)

MenLeft=10-drop

orig=float(1000)

computed=float(10000/MenLeft)

additional=float(computed-orig)

print('Original contribution per person: Php',orig)
print('Additional contribution per person: Php',additional)
print('Computed contribution per person: Php',computed)
