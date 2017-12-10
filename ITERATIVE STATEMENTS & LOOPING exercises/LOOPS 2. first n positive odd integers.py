#2. Write a program that will display the first n positive odd integers.

n=int(input('enter n: '))
counter=1
j=1
while counter <= n:
    if j % 2 != 0:
        print(j)
        counter+=1
    j+=1
