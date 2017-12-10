#1
'''Write a program that will allow the user to enter two integers, start and end.
The program ensures that start is less than or equal to end, then displays numbers from start to end on the screen.'''
start=int(input('start: '))
end=int(input('end: '))
if end < start:
    temp=start
    start=end
    end=temp
while start<=end:
    print(start)
    start+=1

#2
'''Write a program that will allow the user to enter two integers, start and end.
The program ensures that start comes before end, and displays the sum of all numbers from start to end.'''
start=int(input('start: '))
end=int(input('end: '))
if end < start:
    temp=start
    start=end
    end=temp
Sum=0
while start <= end:
    Sum+=start
    start+=1
print(Sum)

#3
'''Write a program that will allow the user to enter a positive integer.
The program displays the digits of this number starting from the rightmost digit. (display reverse)'''
n=int(input('enter positive integer: '))
reverse=''
while n > 0:
    digi=n%10
    n//=10
    reverse+=str(digi)
print(reverse)

#4
'''Write a program that will allow the user to enter a positive integer.
The program forms a new number that is a reverse of the number entered by the user. (compute reverse)
'''
n=int(input('enter positive integer: '))
reverse=0
while n > 0:
    digi=n%10
    n//=10
    reverse=reverse*10+digi
print(reverse)

#5
''' Write a program that will allow the user to enter a positive integer and a digit.
The program forms a new number that is a reverse of the number entered by the user,
and replacing all even digits with digit entered by the user.
Example: number: 123456, digit = 8, output = 183858'''

n=int(input('enter positive integer: '))
n2=int(input('enter a digit: '))
replaced=0
while n > 0:
    digi= n%10
    if digi%2==0:
        digi=n2
    n//=10
    replaced=replaced*10+digi
output=0
while replaced > 0:
    digi2=replaced%10
    replaced//=10
    output=output*10+digi2
print(output)

#6
''' Write a program that will allow the user to enter two positive integers, one and two.
The program forms a new number by attaching the reverse of two (the second input) after the last digit of one (the first input).
Example: one = 1234, two = 9847, output = 12347489
Example: one = 2353, two = 1823, output = 23533281'''
one=int(input('enter positive integer#1: '))
two=int(input('enter positive integer#2: '))
reverseTwo=0
count=1
while two > 0:
    digi2=two%10
    count*=10
    two//=10
    reverseTwo=reverseTwo*10+digi2
print(one*count+reverseTwo)

    





