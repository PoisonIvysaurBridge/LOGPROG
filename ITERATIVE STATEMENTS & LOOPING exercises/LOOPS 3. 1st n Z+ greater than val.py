#3. Write a program that will display the first n positive odd integers greater than val.
val=int(input('enter val: '))
n=int(input('enter n: '))
counter=1
if val % 2 == 0:
    val+=1
else:
    val+=2
while counter <= n:
    if val % 2 != 0:
        print(val)
        counter+=1
    val+=1
