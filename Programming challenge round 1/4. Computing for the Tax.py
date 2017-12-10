'''
4. Computing for the Tax
'''

strInput=input('enter taxable income: ')
income=float(strInput)
basetax=250
remain=income-3000

if remain >= 2000+5000:
    tax= basetax + 0.05*2000 + 0.09*5000 + 0.15*(remain-2000-5000)
    print ('Income tax is: ',tax)

elif remain >= 2000:
    tax= basetax + 0.05*2000 + 0.09*(remain-2000)
    print ('Income tax is: ',tax)

elif remain >= 0:
    tax= basetax + 0.05*remain
    print ('Income tax is: ',tax)

else:
    tax=basetax
    print('Income tax is: ',tax)
