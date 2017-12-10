'''
9. LRT Fare Calculator
'''

strInput=input('entered station (1-15): ')
Enter=int(strInput)
strInput=input('exited station (1-15): ')
Exit=int(strInput)

nStation=Exit-Enter
remain=nStation-3
base=20

if nStation==0:
    base=0

if remain <= 0:
    remain=0

everyS=remain*2.5
print('Php',base+everyS)
