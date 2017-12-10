'''WITH DIFFERENT FILL THIS TIME'''
#right hypotenuse
print('right hypotenuse v.3\n')
h=int(input('height: '))
b=int(input('base: '))
border=input('border? ')
fill=input('fill? ')
k=1
copy=b
while k <= h:
    j=1
    while j <= copy:
        if j==1 or j==copy or k==1 or k==h:
            print(border,end='')
        else:
            print(fill,end='')
        j+=1
    copy-=1
    print()
    k+=1

print('\nright hypotenuse v.4\n')   
n=int(input('n: '))
border=input('border? ')
fill=input('fill? ')
k=1
copy=1
while k <= n:
    j=1
    while j <= copy:
        if j==1 or j==copy or k==1 or k==n:
            print(border,end='')
        else:
            print(fill,end='')
        j+=1
    copy+=1
    print()
    k+=1  
    
#left hypotenuse
print('\nleft hypotenuse v.3')
n=int(input('n: '))
border=input('border? ')
fill=input('fill? ')
k=1
copy=n
while k <= n:
    j=1
    while j <= n:
        if j >= copy:
            print(border,end='')
        else:
            print(' ',end='')
        j+=1
    copy-=1
    print()
    k+=1

print('\nleft hypotenuse v.4')
n=int(input('n: '))
border=input('border? ')
fill=input('fill? ')
k=1
copy=1
while k <= n:
    j=1
    while j <= n:
        if j >= copy:
            print(border,end='')
        else:
            print(' ',end='')
        j+=1
    copy+=1
    print()
    k+=1
