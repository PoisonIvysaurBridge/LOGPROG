n=1
j=1
while j <= 3:
    factor=1
    Sum=0
    while n%factor ==0:
        Sum+=factor
        factor+=1
    if Sum==n and Sum!=1:
        print(n)
        j+=1
    n+=1
