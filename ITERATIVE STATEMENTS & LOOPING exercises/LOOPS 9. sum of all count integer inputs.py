# LOOPS 1
'''
9. Write a program that will allow the user to enter an integer value count, and allow the user to enter count integer

inputs. After all inputs are given, the program displays the sum of these input values.
'''
count=int(input('enter positive integer: '))
Sum=0
j=1
while j <= count:
    n=int(input('enter number: '))
    j+=1
    Sum += n
print(Sum)
