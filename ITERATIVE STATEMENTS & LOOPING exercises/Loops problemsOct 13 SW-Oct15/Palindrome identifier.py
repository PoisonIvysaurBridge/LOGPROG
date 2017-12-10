#Palindrome identifier
n=int(input('n: '))
rev=0
check=n
while n > 0:
    rev=rev*10+n%10
    print(n%10)
    n=n//10
if check==rev:
    print('The number is a palindrome.')
else:
    print('Not a palindrome')

