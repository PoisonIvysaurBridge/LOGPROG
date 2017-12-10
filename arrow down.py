n=int(input("n: "))
if n%2 != 0:
    jlimit=3*n
else:
    jlimit=3*n+1
copy1=jlimit//2+1
copy2=jlimit//2+1
inner1=1#
inner2=1#
k=1
while k <= 3*n:
    if k==n+1:
        copy1=1
        copy2=jlimit
    j=1
    while j <= jlimit:
        
        if j>= copy1 and j<=copy2:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    k+=1
    print()
    if k>2 and k<n+1:
        copy1-=1
        copy2+=1
    elif k>n+1 and k<=2*n:
        copy1+=1
        copy2-=1
            
    
        
