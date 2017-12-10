#train problem in 1st dep ex


a = int(input('Enter number of males:'))
f = int(input('Enter number of females:'))


if a%20 == 0:
    ma = a//20
    c = 20
else:
    ma = a//20+1
    c = a%20


ft = f - 10*ma

if ft <= 0 or ft-(20-c) <=0:
    print('Number of trains needed: '+str(ma))
else:
    print('Number of trains needed: '+str(1+(ft-(20-c))//30+ma))


