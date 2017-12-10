#multiplication table
print('===MULTIPLICATION TABLE===')
n=int(input('enter number: '))
Range= int(input('enter range: '))
for i in range (Range+1):
    print(str(n)+'*'+str(i)+'=',n*i)
    i+=1

print('==========================')
