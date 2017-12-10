'''
Exercise 1
Write a program that determines if a number is odd or even.
S.
'''

strInput=input('enter number: ')
n=int(strInput)

if n%2==0 and n!=0:
    print('even')

elif n%2!=0:
    print('odd')

else:
    print('it is 0')



#LOOP experiment hahahaha
while True:
    strInput=input('enter number: ')
    n=int(strInput)

    if n%2==0 and n!=0:
        print('even')

    elif n%2!=0:
        print('odd')

    else:
        print('it is 0')
