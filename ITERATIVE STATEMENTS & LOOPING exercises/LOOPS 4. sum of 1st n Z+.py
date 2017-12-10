#4. Write a program that will compute for the sum of the first n positive integers.
Sum=0
counter=1
j=1
n=int(input('enter n: '))
while counter <= n:
    Sum=Sum+j
    j+=1
    counter += 1
print(Sum)
