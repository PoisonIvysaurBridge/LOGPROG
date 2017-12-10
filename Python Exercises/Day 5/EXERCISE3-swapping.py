'''Exercise 3
Complete the program so that it will interchange the values of two
variables.

Code:
strInput = input ("Enter a number: ")
x = int (strInput)
print ("x = ", x)
strInput = input ("Enter another number: ")
y = int (strInput)
print ("y = ", y)
#put your code here
print ("nnafter swap...nn x = ", x)
print ("y = ", y)
'''

strInput=input('Enter a number: ')
x=int(strInput)
print('x=',x)

strInput=input('Enter a number: ')
y=int(strInput)
print('y=',y)

#WHAT TIMES IS IT? SWAPPING TIME!!!
z=x
w=y
x=w
y=z


print('\nafter swap...')
print('x=',x)
print('y=',y)

#BETTER SOL'N: USE ONLY ONE TEMPORARY VARIABLE
temp=x
x=y
y=temp

#or...
temp=y
y=x
x=temp

