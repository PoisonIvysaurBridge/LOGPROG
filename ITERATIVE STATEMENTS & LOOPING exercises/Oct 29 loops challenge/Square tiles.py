col=int(input("columns: "))
row=int(input("rows: "))
squares=0
smaller=col
if row < col:
    smaller=row
j=0
while j <= smaller:
    squares=squares+(col-j)*(row-j)
    j+=1
print(squares)

squares=0
col=int(input("columns: "))
row=int(input("rows: "))
smaller=col
if row < col:
    smaller=row
m=1
while m <=smaller:
    j=1
    while j<=col:
        k=1
        while k<=row:
            if m+k <=row and m+j<=col:
                squares+=1
            k+=1
        j+=1
    m+=1
print(squares+col*row)
