# HOMEWORK
'''
1. Write a program that will allow the user to enter a positive integer value. The program displays the number of digits

of the input.

Enter a number: 1234

Number of digits: 4

Enter a number: 34530

Number of digits: 5
'''

n=int(input('Enter a number: '))
count=0
if n==0:     #0 is a digit
    count=1
while n > 0:
    n = n//10
    count += 1
print('Number of digits:',count)
        
