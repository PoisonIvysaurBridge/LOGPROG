'''Exercise 4
Write a program that will allow the user to enter an 8-digit number to
represent a date value (with the format of mmddyyyy). The rst 2 digits
of this number represent the month, next 2 digits the day and the last 4
digits represent the year.'''

strInput=input('Enter a number: ')
n=int(strInput)

year=n%10000
year=int(year)

day=(n%1000000-n%10000)/10000
day=int(day)

month=(n%100000000-n%1000000)/1000000
month=int(month)

print('month=',str(month)+',','day=',str(day)+',','year=',year)

#Better sol'n would be...
year=n%10000

day= n //10000 %10

month=n//1000000
# no need to put int()
