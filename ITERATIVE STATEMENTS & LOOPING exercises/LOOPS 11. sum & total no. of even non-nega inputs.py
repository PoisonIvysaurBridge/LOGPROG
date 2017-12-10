'''
11. Write a program that will allow the user to continuously input non-negative integer values. Input ends when the user
enters a negative value. After all inputs are given, the program displays number of positive even inputs and the sum of
all the non-negative even inputs.
'''
n=int(input('enter n: '))
count=0
Sum=0
while n >= 0:
    if n % 2 == 0:
        Sum+=n
        count+= 1
    n=int(input('enter n: '))
print('total number of even inputs:', count)
print('sum of all the non-negative even inputs:',Sum)
