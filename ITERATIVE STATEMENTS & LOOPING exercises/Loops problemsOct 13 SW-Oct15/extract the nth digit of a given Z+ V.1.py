#extract the nth digit of a given Z+ VERSION 1
num= int(input('Enter a number: '))
n=int(input('nth place: '))
display=0

while n>0:
    display= num%10
    num//=10
    n-=1
print(display)

'''
OR
j=1
while j <= n:
    display= num%10
    num//=10
    j+=1
'''
