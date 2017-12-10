'''
extract the nth digit of a given Z+
example:
num=12345        >>>4
nth=4

num=5678         >>>6
nth=2

num=5678         >>>0
nth=5
'''
num= int(input('Enter a number: '))
rev=0
while num > 0:
    rev=rev*10 + num%10
    num=num//10

n=int(input('nth place: '))
display=0
j=1
while j <= n:
    display= rev%10
    rev//=10
    j+=1
print(display)
