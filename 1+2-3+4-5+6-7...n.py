'''
Write  program that computes for
1 + 2 – 3 + 4 – 5 + … + n
'''





#1 - 2 + 3 - 4 + 5 - … - n
n=int(input('n: '))
Sum=0
j=1
while j <= n:
    if j % 2 == 0:
        Sum=Sum-j
    else:
        Sum=Sum+j
    j=j+1
print(Sum)


