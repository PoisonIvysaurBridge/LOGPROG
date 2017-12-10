# DECIMAL TO OCTAL CONVERTER
n=int(input("n: "))
copy=n
octal=0
j=0  #place value counter
while copy>0:
    octal= octal*10 + copy%8
    copy//=8
    if copy%8 == 0:
        j+=1
rev=0
while octal>0:
    rev= rev*10 + octal%10
    octal//=10
while j>0:
    rev*=10
    j-=1
print(rev)
