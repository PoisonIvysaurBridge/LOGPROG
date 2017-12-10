#2
m=6
n=0
h=1
while h <= m:
    z=2*h
    n=n+z
    print("H=",h,"Z=",z,"N=",n )
    h+=1
#4
i=2
while i <= 4:
    j=5
    while j >=3:
        print(i+j)
        j-=1
    i+=1

#5
i=1
while i <= 5:
    j=1
    while j < i:
        print("*",end='')
        j+=1
    print()
    i+=1

#26
num1=7
num2=4
x=1
while x <= num2:
    y=1
    while y <= num2-x:
        print(y,end="")
        y+=1
    y=1
    while y <= x:
        print(num1,end='')
        num1=(num1+1)%10
        y+=1
    print()
    x+=1

#27 infinite loop

#28
