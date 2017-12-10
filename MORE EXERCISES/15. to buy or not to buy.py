'''
15. to buy or not to buy
'''

strInput=input('enter current date: ')
cdate=int(strInput)
strInput=input('enter expiration date: ')
exdate=int(strInput)

cmonth= cdate// 1000000
cday= cdate//10000%100
cyear= cdate% 10000

exmonth= exdate//1000000
exday= exdate//10000%100
exyear= exdate%10000

if cyear < exyear:
    print('buy')

elif cyear==exyear:
    if cmonth <= exmonth:
        if cday < exday:
            print('buy')

        else:
            print('do not buy')
    else:
        print('do not buy')
else:
    print('do not buy')
