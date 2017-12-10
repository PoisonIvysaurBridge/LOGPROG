'''
4. Area or Perimeter
'''

strInput=input('enter length: ')
L=float(strInput)
strInput=input('enter width: ')
W=float(strInput)

AoP=input('Are or Perimeter? ')

if AoP=="Area":
    A=L*W
    print(A)

elif AoP=="Perimeter":
    P=2*L + 2*W
    print(P)

else:
    print('invalid input')
