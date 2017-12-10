#find the GCD of 2 integers
gcd=1
num1=int(input('number1: '))
num2=int(input('number2: '))
factor=2
while num1 >= factor and num2 >= factor:
    if num1%factor==0 and num2%factor==0:
        gcd=gcd*factor
        num1//=factor
        num2//=factor
    else:
        factor+=1
print(gcd)
