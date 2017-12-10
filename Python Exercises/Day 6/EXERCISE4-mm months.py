'''
Exercise 4
Write a program that will accept as input an integer, assuming the
following format mmddyyyy. Depending on the value in mm, display the
corresponding month in words. If mm is 1, display \January"; if 2, display
\February", and so on.
S.
'''

strInput=input('enter date: ')
n=int(strInput)

month=n//1000000
mm=month

if month==10:
    print('October')

elif month==11:
    print('November')

elif month==12:
    print('December')
    
elif mm==1:
    print('Janurary')

elif mm==2:
    print('February')

elif mm==3:
    print('March')

elif mm==4:
    print('April')

elif mm==5:
    print('May')

elif mm==6:
    print('June')

elif mm==7:
    print('July')

elif mm==8:
    print('August')

elif mm==9:
    print('September')

else:
    print('Did you entered exactly 8 digits? :)')


