'''
x^1   x^2   x^3         x^n
--- + --- + --- + ... + --- , where n is even
 1!   2!    3!           n!
'''
x=int(input("x: "))
n=int(input("n: "))
Sum=0
j=1
while j<=n:
    k=1
    fac=1
    exp=1
    while k<=j:
        fac*=k
        exp*=x
        k+=1
    j+=1
    Sum+=exp/fac
print(Sum,exp,fac)

# shorter method (one single loop)
x=int(input("x: "))
n=int(input("n: "))
Sum=0
j=1
exp=x
fac=j
while j<=n:
    Sum+=exp/fac
    fac*=j+1
    exp*=x
    j+=1
print(Sum,exp,fac)
