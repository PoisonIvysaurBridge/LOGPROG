'''Practice 1
Write a program that displays the reverse of an input 3-digit number while
retaining it as a whole.
S.'''

strInput=input('enter number: ')
n=int(strInput)

n1=n%10
n1=int(n1)

n2=(n%100-n%10)/10
n2=int(n2)

n3=(n-n%100)/100
n3=int(n3)

print('reverse is: ',str(n1)+str(n2)+str(n3))

#better solution...
'''
while retaining it as a whole!!!
so no str() and +

nVal=pne*100+ten*10+hundred
'''
