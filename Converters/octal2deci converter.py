# OCTAL TO DECIMAL CONVERTER
n=int(input("n: "))
copy=n
rev=0
while copy>0:
    rev=rev*10 + copy%10
    copy//=10
deci=0
while rev>0:
    deci*=8
    deci= deci + rev%10
    rev//=10
print(deci)


    
