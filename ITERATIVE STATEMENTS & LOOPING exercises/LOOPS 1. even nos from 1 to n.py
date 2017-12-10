#1. Write a program that will display positive even numbers from 1 to n.

n= int(input('enter n: '))
j=1
while j <= n:
     if j % 2 == 0:
          print(j)
     j+=1
