# HOMEWORK
'''
3. Write a program that will allow the user to enter a positive integer value. The program computes for the reverse of

the input.

Enter a number: 1234

Reverse: 4321

Enter a number: 34530

Reverse: 3543
'''

count= -1
place= 1
n= int(input('Enter a number: '))
result=0
while n > 0:
    digit= n%10
    result= result + digit*place
    place= place/10
    count += 1
    n= n//10
final= result*10**count
print(int(final))

#better code
n= int(input('Enter a number: '))
result=0
while n > 0:
    result=result*10 + n%10
    n=n//10
print(result)


