'''a program that will display the digit at the tens place of a given
non-negative integer value.'''

n=input('Please enter a non-negative integer value: ')
n=int(n)
TensOnes=n%100
Ones=n%10
TensDigit=(TensOnes-Ones)/10
print(int(TensDigit))
