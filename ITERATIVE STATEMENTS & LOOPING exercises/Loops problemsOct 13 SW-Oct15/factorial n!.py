
n=int(input('n: '))
Sum=0

k=1
while k<=n:
    facCnt=1
    fac=1
    while facCnt<=k:
        fac*=facCnt
        facCnt+=1
    k+=1
print(fac)
