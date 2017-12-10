'''
x^2   x^4   x^6         x^n
--- + --- + --- + ... + --- , where n is even
 1!   2!    3!           n!
'''

x=int(input("x: "))
n=int(input("n: "))
Sum=0
j=1
k=1
while j<=n:
    fac=1
    facj=1
    while facj<=k:
        fac*=facj
        facj+=1
    if j%2==0:
        exp=1
        expj=1
        while expj<=j:
            exp*=x
            expj+=1
        Sum+=exp/fac
        k+=1
    j+=1
print(Sum)

