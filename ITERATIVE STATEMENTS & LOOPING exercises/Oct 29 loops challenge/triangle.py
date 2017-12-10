''' ######### CODE OF MISS    #############################################'''
# upside down triangle
print()
print('CODE OF MISS')

n=int(input('n: '))
copy=1
k=1
while k <= n:
    j=1
    while j <= 2*n:
        if j==k or j+k== 2*n:
            print('*',end="")
        else:
            print(" ",end='')
        j+=1
    copy+=1
    k+=1
    print()
