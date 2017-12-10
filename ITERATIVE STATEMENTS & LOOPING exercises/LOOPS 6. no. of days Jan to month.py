'''
6. Write a program that will compute for the number of days from January until month. month may be any value between
1 - 12.
'''
Sum=0
start=1
month=int(input('enter month ended: '))
while start <= month:
    if start==2:
        days=28
    elif start==4 or start==6 or start== 9 or start==11:
        days=30
    else:
        days=31
    Sum=Sum+days
    start+=1
print(Sum)
    
