
nWidth=int(input('enter width: '))
nLength=int(input('enter length: '))
k=1
while k<= nWidth:
    j=1
    while j<= nLength:
        if j==1 or k==1 or j==nLength or k==nWidth:
            print('*',end='')
        else:
            print(' ',end='')
        j+=1
    print()
    k+=1
    
b=int(input("base: "))
h=int(input("height: "))
copy=h
k=1
while k <= h:
    j=1
    cnt=1
    while j <= b:
        if j >= copy:
            print(cnt,"",end="")
            cnt+=1
        else:
            print(" ",end="")
        j+=1
    copy-=1
    k+=1
    print()
