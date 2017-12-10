#my complex problem V.2
x=int(input('x: '))
n=int(input('n: '))
Sum=0

j=1
while j<=n:
    if j%2==0:
        xcount=1
        xRaised=1
        while xcount<=j:
            xRaised*=x
            xcount+=1
    j+=1
    print(xRaised)

k=1
while k<=n:
    facCnt=1
    fac=1
    while facCnt<=k:
        fac*=facCnt
        facCnt+=1
    k+=1
    print(fac)

Sum+=xRaised/fac
