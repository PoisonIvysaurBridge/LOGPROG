'''n=int(input("enter number: "))
j=0
rev=0
while n > 0:
    digit=n%10
    n//=10
    rev=rev*10+digit
    j+=1
    if j=3:
        triplet=0
        converted=''
        while rev>0:
            triplet= triplet*10+rev%10
            converted=converted+str(triplet)
            
        j=0'''

n=int(input("enter number: "))
triplet=0
while n > 0:
    triplet=triplet*1000+n%1000
    n//=1000
print(triplet)    
converted=0
while triplet > 0:
    converted=triplet%1000
    triplet//=1000
    if triplet!=0:
        print(str(converted)+',',end='')
    else:
        print(str(converted))
#print(converted)
    
