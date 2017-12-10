'''
14. How Old Are You?
Write a program that asks for the current date (as an integer assuming the format mmddyyyy). You
may use the numbers 1-12 to represent the month for convenience. After that, the program should also
ask for the birthday of the user (as an integer assuming the format mmddyyyy). The program should
display how old the user is. For example, if today is September 18, 2015 and the user's birthday is
September 29, 1992, then the user is 22 years old.
'''

strInput=input('enter current date (mmddyyyy): ')
cdate=int(strInput)
strInput=input('enter birth date (mmddyyyy): ')
bdate=int(strInput)

cmonth= cdate// 1000000
cday= cdate//10000%100
cyear= cdate% 10000

bmonth= bdate//1000000
bday= bdate//10000%100
byear= bdate%10000

age= cyear-byear

if cmonth > bmonth:
    print(age,'years old')

elif cmonth==bmonth:
    if cday < bday:
        age=age-1
    print(age,'years old')

else:
    print(age-1)

#shorter code:
    strInput=input('enter current date (mmddyyyy): ')
cdate=int(strInput)
strInput=input('enter birth date (mmddyyyy): ')
bdate=int(strInput)

cmonth= cdate// 1000000
cday= cdate//10000%100
cyear= cdate% 10000

bmonth= bdate//1000000
bday= bdate//10000%100
byear= bdate%10000

age= cyear-byear

if cmonth >= bmonth:
    if cday < bday:
        age=age-1
    print(age,'years old')

else:
    print(age-1)





