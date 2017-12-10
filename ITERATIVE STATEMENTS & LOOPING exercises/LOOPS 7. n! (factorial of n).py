#7. Write a program that will compute for n! (factorial of n).
n=int(input('enter n: '))
product=1
j=1
while j <= n:
    product=product*j
    j+=1
print(product)
