# X^n
x=int(input('x: '))
n=int(input('n: '))

#if n is negative
negexp=False
if n<0:
    negexp=True
    n=n*-1

j=1
product=1
while j <= n:
    product=product*x
    j+=1

#if n is negative    
if negexp==True:
    product= 1/product

print (product)


