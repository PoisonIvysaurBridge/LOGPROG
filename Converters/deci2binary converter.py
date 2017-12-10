# DECIMAL TO BINARY CONVERTER
n=int(input("n: "))
b128= n//128
n= n%128
b64= n//64
n= n%64
b32= n//32
n= n%32
b16= n//16
n= n%16
b8= n//8
n= n%8
b4= n//4
n= n%4
b2= n//2
n= n%2
b1=n
converted=str(b128)+str(b64)+str(b32)+str(b16)+str(b8)+str(b4)+str(b2)+str(b1)
print(converted)

# loop version
n=int(input("enter decimal number from 0 to 255: "))
converted=''
divisor=128
while n > 0:
    if n//divisor > 0:
        converted+= str(n//divisor)
    else:
        converted+= str(n//divisor)
    n=n%divisor
    divisor//=2
print(converted)
        
