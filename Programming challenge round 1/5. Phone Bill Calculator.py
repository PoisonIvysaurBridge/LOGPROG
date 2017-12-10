'''
5. Phone Bill calculator
'''

strInput=input('enter 12-digit phone no.: ')
nPhone=int(strInput)
strInput=input('enter start time: ')
start=int(strInput)
strInput=input('enter end time: ')
end=int(strInput)

HH1=start//100
MM1=start%100
HH2=end//100
MM2=end%100

if HH1 > HH2:
    HH2=HH2+24

start=HH1*60 + MM1
end= HH2*60 + MM2
duration = end - start

print('call duration',duration,'minutes')

areacode=nPhone//10000000000
netwk=nPhone%10000000 %1000

if areacode!= 63:
    charge= 16.5
    pBill= duration*charge
    print ('total bill is',pBill)

elif netwk==905 or netwk==906 or netwk==916 or netwk==918:
    base=8
    remain= duration-2
    pBill= base+remain*1.00
    print ('total bill is',pBill)

else:
    base=10
    remain=duration-2
    pBill=base+remain*1.5
    print ('total bill is',pBill)


