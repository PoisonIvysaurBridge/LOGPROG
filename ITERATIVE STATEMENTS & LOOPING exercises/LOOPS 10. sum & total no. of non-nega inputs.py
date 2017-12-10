'''
10. Write a program that will allow the user to continuously input non-negative integer values. Input ends when the user
enters a negative value. After all inputs are given, the program displays the input values, the total number of inputs
and the sum of all the non-negative inputs.
'''
n=int(input('enter n: '))
count=1
Sum=0
while n > 0:
    Sum+=n
    n=int(input('enter n: '))
    count+= 1
print('total number of inputs:', count)
print('sum of all the non-negative inputs:',Sum)
