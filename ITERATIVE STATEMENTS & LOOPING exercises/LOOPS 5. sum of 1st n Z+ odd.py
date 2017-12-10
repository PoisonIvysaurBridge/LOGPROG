#5. Write a program that will compute for the sum of the first n positive odd integers.
Sum=0
counter=1
j=1
n=int(input('enter n: '))
while counter <= n:
    if j % 2 != 0:
        Sum=Sum+j
        counter+=1
    j+=1
print(Sum)
