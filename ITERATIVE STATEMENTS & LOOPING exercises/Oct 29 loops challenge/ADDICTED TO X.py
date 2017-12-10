#addicted to X
n=int(input("n: "))
copy1=1
copy2=n
k=1
while k <= n:
    j=1
    while j<=n:
        if j==copy1 or j==copy2:
            print("X",end="")
        else:
            print(" ",end="")
        j+=1
    k+=1
    copy1+=1
    copy2-=1
    print()


# DEPEX 2 last programming problem
n=int(input("n: "))
copy=2*n
copy2=2
k=1
while k <= 2*n-1:
    j=1
    while j<=2*n+1:
        if j==copy2 or j==copy:
            print(" ",end="")
        else:
            print("@",end="")
        j+=1
    k+=1
    copy-=1
    copy2+=1
    print()
# OR
n=int(input("n: "))
copy=2*n
k=1
while k <= 2*n-1:
    j=1
    while j<=2*n+1:
        if j==k+1 or j==copy:
            print(" ",end="")
        else:
            print("@",end="")
        j+=1
    k+=1
    copy-=1
    print()


