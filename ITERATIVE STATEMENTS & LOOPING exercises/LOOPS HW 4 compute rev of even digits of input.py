# HOMEWORK
'''
4. Write a program that will allow the user to enter a positive integer value. The program computes for the reverse of

the input containing only the even-valued digits.

Enter a number: 1234

Reverse (even digits only): 42

Enter a number: 34530

Reverse (even digits only): 0
'''

count= -1
place= 1
n= int(input('Enter a number: '))
result=0
while n > 0:
    digit= n%10
    if digit %2==0:
        result += digit*place
        place /= 10
        count += 1
    n //= 10
    
final= result*10**count
print(int(final))
