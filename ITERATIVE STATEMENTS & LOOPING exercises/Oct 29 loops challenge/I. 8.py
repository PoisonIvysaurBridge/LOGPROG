n=int(input('n: '))
copy=1
k=1
while k <= n:
    j=1
    while j <= n:
        if j >= copy:
            if j==copy or j==n:
                print('* ',end='')
            else:
                print('  ',end='')
        else:
            print(' ',end='')
        j+=1
    copy+=1
    print()
    k+=1

copy=1
k=1
while k <= n:
    j=1
    while j <= 2*n:
        if j >= copy:
            if j+k==2*n or j==k:
                print('*',end='')
            else:
                print(' ',end='')
        else:
            print(' ',end='')
        j+=1
    copy+=1
    print()
    k+=1
