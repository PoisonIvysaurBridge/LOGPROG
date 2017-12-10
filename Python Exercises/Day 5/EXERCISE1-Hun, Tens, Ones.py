'''Exercise 1
Write a program that displays each digit of the user's input on the screen.
Assume that the user will enter at most a 3-digit number.'''

strInput=input('Enter a number: ')
n=int(strInput)
Hundreds=(n-n%100)/100
Tens=(n%100-n%10)/10
Ones=n%10
print('Hundreds=',int(Hundreds))
print('Tens=',int(Tens))
print('Ones=',int(Ones))

'''
alternative solution!!! a better way!

strInput=input('Enter a number: ')
n=int(strInput)
'''
#better code is:
Hundreds=n//100
Tens=n%100//10
Ones=n%10
'''
print('Hundreds=',int(Hundreds))
print('Tens=',int(Tens))
print('Ones=',int(Ones))
'''
