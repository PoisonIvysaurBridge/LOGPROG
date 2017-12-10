# diamond

n=int(input("n: "))
copy1=(n+1)//2
copy2=(n+1)//2
k=1
while k<=n:
    j=1
    while j<=n:
        if j>=copy1 and j<=copy2:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    k+=1
    if k>(n+1)//2:
        copy1+=1
        copy2-=1
    else:
        copy1-=1
        copy2+=1
    print()
