'''
Exercise 2
Write a program that determines if a number is divisible by 8. If it is,
display divisible by 8, otherwise, display not divisible by 8 and display
the remainder when dividied by 8.
S.
'''

strInput=input('enter number: ')
n=int(strInput)

if n%8==0:
    print('divisible by 8')

else:
    print('not divisible by 8\n'"remainder:",n%8)
