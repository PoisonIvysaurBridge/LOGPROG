'''
12. Write a program that will allow the user to enter a positive integer value. The program displays the digits of this value

in reverse order.

Enter a number: 1234

Display in reverse: 4321

Enter a number: 34530

Display in reverse: 03543
'''

place=''
n= int(input('Enter a number: '))
while n > 0:
    digit= n%10
    convert= str(digit)
    place= place+convert
    n= n//10
print('Display in reverse:',place)

