n=int(input("n: "))
even=True
if n%2 != 0:
    jlimit=3*n
    even=False
else:
    jlimit=3*n+1
copy1=jlimit//2+1
copy2=jlimit//2+1
inner1=jlimit//2+1
inner2=jlimit//2+1
'''if even==True:
    inner2=2*n+1
else:
    inner2=2*n'''
k=1
while k <= 3*n:
    if k==n:
        copy1=1
        copy2=jlimit
    if k==2*n+1:
        copy1=copy1
        copy2=copy2
    j=1
    while j <= jlimit:
        if k>3*n-2 and j>=inner1 and j<=inner2:
            print(" ",end="")
        elif j>= copy1 and j<=copy2:
            print("@",end="")
        
        else:
            print(" ",end="")
        j+=1
    k+=1
    print()
    if k<n or k>=2*n:
        copy1-=1
        copy2+=1
    elif k>n and k<2*n:
        copy1+=1
        copy2-=1
    if k>=2*n:
        inner1-=1
        inner2+=1
    
        
            
    
        
