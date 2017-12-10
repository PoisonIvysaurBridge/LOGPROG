# HOMEWORK
'''
2. Write a program that will allow the user to enter a positive integer value. The program displays in reverse the even-
valued digits.

Enter a number: 1234

Display even-digits in reverse: 42

Enter a number: 5397131

Display even-digits in reverse:

'''

place=''
n= int(input('Enter a number: '))
while n > 0:
    digit= n%10
    if digit%2==0:
        convert= str(digit)
        place= place+convert
    n= n//10
print('Display even-digits in reverse:',place)
