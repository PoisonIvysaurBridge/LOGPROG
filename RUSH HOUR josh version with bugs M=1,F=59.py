# RUSH HOUR
m = int(input('Enter number of males:'))
f = int(input('Enter number of females:'))


if m%20 == 0:
    m2 = m//20
    c = 20
else:
    m2 = m//20+1
    c = m%20


f2 = f - 10*m2

if f2 <= 0 or f2-(20-c) <=0:
    print('Number of trains needed: '+str(m2))
else:
    print('Number of trains needed: '+str(1+(f2-(20-c))//30+m2))


