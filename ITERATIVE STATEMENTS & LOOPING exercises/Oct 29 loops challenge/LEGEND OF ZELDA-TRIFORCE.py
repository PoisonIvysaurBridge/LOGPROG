
n=int(input("n: "))
inner1=n+1
inner2=3*n
copy1=2*n
copy2=2*n+1
k=1
while k<= 2*n:
    j=1
    while j<= 4*n:
        if j==copy1:
            print("/",end="")
        elif j==copy2:
            print("\\",end="")
        
        elif j==inner1 and k==inner1:
                print("\\",end="")
        elif j==inner2 and j+k==4*n+1:
                print("/",end="")

        elif k%n==0 and j>copy1 and j<copy2:# or k%n==0 and j>copy1 and j<copy2:# and j!=2*n and j!=2*n+1:
            print("_",end="")
        #elif j>copy1 and j<copy2:  with fill
         #   print("@",end="")
        else:
            print(" ",end="")
        j+=1
    copy1-=1
    copy2+=1
    
    if k>n:
        inner1+=1
        inner2-=1
    k+=1
    print()
