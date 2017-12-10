x=int(input('x: '))
n=int(input('n: '))
negExp=0
if n < 0:
    negExp=1
    n=b*-n
j=1
product=1
while j <= n:
    product=product*x
    j+=1

if negExp==1:
    product=1/product
print(product)
    
