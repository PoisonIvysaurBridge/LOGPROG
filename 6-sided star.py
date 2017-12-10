n=int(input("n: "))

jlimit=n*2 + n + (1+n%2)
klimit=(n-1)*2 + 2*n-1
copy1=jlimit//2+1
copy2=jlimit//2+1
k=1
while k <= klimit:
    if k==n:
        copy1=1
        copy2=jlimit
    if k==(n-1) + (2*n-1)+1:
        copy1=n
        copy2=jlimit-(n-1)
    j=1
    while j <= jlimit:
        if j>= copy1 and j<=copy2:
            print("@",end="")
        
        else:
            print(" ",end="")
        j+=1
    k+=1
    print()
    if k<n or k>=2*n and k<= (2*n-1)+(n-1):
        copy1-=1
        copy2+=1
    elif k>n:
        copy1+=1
        copy2-=1
    
    
    
        
            
    
        
