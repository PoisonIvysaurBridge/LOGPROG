n=int(input("n: "))
copy=n
k=1
while k <= n:
    j=1
    cnt=1
    while j <= n:
        if j >= copy:
            print(cnt,"",end="")
            cnt+=1
        else:
            print(" ",end="")
        j+=1
    copy-=1
    k+=1
    print()
    
print()
copy=1
k=1
while k <= n:
    j=1
    cnt=1
    while j <= n:
        if j >= copy:
            print(cnt,"",end="")
            cnt+=1
        else:
            print(" ",end="")
        j+=1
    copy+=1
    k+=1
    print()
