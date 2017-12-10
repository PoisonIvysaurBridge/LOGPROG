n=int(input("n: "))
lowestOdd="no odd integer"
if n%2!=0:
    lowestOdd=n

while n >=1:
    
    if lowestOdd!="no odd integer" and n < lowestOdd and n%2!=0:
        lowestOdd=n
    n=int(input("n: "))
print(lowestOdd)
