'''
Exercise 3
Write a program that converts a military time input to its equivalent
12-hour format. Note that:
The input of the user is an integer assuming the format hhmm.
The valid hour value in the military time format is [00; 23].
The valid minute value in the military time format is [00; 59].
Only valid military time inputs will be converted to the equivalent
12-hour format. Display an error message for invalid input.
'''

strInput=input('enter military time (hhmm): ')
milTime=int(strInput)

hh= milTime//100
mm= milTime%100

if (hh >= 0 and hh <= 23) and (mm >= 0 and mm <= 59): 
        
    if hh >= 12:
        POD = "PM"  #POD stands for period of the day
    else:
        POD = "AM"
       
    
    
    if hh%12 == 0:
        hh= 12
        
        if mm < 10:
            print(str(hh)+':0'+str(mm),POD)
        else:
            print(str(hh)+':'+str(mm),POD)

    else:
        hh=hh%12
        
        if mm < 10:
            print(str(hh)+':0'+str(mm),POD)
        else:
            print(str(hh)+':'+str(mm),POD)
    
else:
    print ('Invalid input')




# Sol'n of miss

strInput=input('enter military time (hhmm): ')
milTime=int(strInput)

nHr= milTime//100
nMin= milTime%100

if hh >= 0 and hh <= 23 and mm >= 0 and mm <= 59: 
        
    if nHr >= 12:
        if nHr > 12:  #
            nHr= nHr%12
        print(nHr,':',nMin,'p.m.')
       
    else:
        if nHr==0:
            nHr=12
        print(nHr,':',nMin,'a.m.')
       
    
else:
    print ('Invalid input')

    
