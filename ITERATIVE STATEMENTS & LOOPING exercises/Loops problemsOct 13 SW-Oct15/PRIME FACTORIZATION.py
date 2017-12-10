# PRIME FACTORIZATION
x=int(input('x: '))
if x <= 1:
    print('no primes to factor')
else:
    j=2
    while j < x and x % j != 0:
        j+=1
    if j == x:
        print(x)
    else:
        while j <= x:
            while x % j == 0:
                print(j)
                x=x//j

            j+=1


