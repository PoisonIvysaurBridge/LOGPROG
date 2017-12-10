# 1! + 2! + 3! + ... + n!
n=int(input('n: '))
Sum=0
j=1
while j <= n:
    count=1
    factorial=1
    while count <= j:
        factorial*=count
        count+=1
    j+=1
    Sum+=factorial
print(Sum)
