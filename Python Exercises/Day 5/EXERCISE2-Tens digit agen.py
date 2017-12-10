'''Exercise 2
Write a program that will display the digit at the tens place of a given
non-negative integer value.'''

strInput=input('Please enter a non-negative integer value: ')
n=int(strInput)
TensDigit=(n%100-n%10)/10
print('Tens=',int(TensDigit))

'''
better sol'n:

strInput=input('Please enter a non-negative integer value: ')
n=int(strInput)
'''
#better code is:
TensDigit=n%100//10
'''
print('Tens=',int(TensDigit))
'''
