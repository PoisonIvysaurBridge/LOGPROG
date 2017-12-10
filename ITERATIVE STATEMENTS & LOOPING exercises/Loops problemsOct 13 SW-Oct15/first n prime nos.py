n=int(input("n: "))
j=1
x=2
while j <= n:
    factor=2
    while factor < x and x%factor!=0:
        factor+=1
    if factor==x:
        print(factor)
        j+=1
    x+=1
