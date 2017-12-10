#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
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
