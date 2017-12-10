#PRIME FACTORIZATION optimized code version 
x=int(input('x: '))
if x <= 1:
    print('no primes to factor')
else:
    j=2
    while j <= x:
        while x % j == 0:
            print(j,end=' ')
            x=x//j
        j+=1
print()
#another code by miss
num=int(input('enter number: '))
factor=2
while factor<=num:
    if num % factor == 0:
        print(factor,end=' ')
        num//=factor
    else:
        factor+=1
print("hi")
