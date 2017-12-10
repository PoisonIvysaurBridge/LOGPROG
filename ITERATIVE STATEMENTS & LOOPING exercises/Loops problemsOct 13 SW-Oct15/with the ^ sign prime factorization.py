#with the caret (^) sign
count=0
num=int(input('enter number: '))
factor=2
x=factor
while num > 0:
    if num % factor == 0:
        num//=factor
        if factor==x:
            count+=1
        else:
            if count > 0:
                print(str(x)+'^'+str(count))
            print(str(factor))#+'^1')
            count=0
            #x+=1
    else:
        factor+=1
        
