# prime or not prime

x=int(input('x: '))
if x <= 1:
    print('cannot be classified since it is less than or equal to 1')
else:
    j=2
    while j< x and j%x!=0:
        j+=1
    if j==x:
        print('prime')
    else:
        print('not prime')
        
