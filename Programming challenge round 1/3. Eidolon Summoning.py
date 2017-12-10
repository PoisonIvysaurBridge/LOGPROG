'''
3. Eidolon Summoning 
'''

strInput=input('enter year: ')
year=int(strInput)
v=0

if year %6 ==0:
    print('Phoenix has come forth! – Wish for health!')
    v=1
    if (year/6) - (year//100*100)//6==3:
        print('Leviathan has come forth! – Wish for peace!')
    
if year %50 ==0:
    print('Bahamut has come forth! – Wish for wisdom!')
    v=1

if v==0:
    print('Too bad. No Eidolon(s) will visit for the year.')

