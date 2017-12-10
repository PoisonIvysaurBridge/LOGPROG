'''
1. Color Mixer
'''

strInput=input('enter 1st color: ')
first =strInput
strInput=input('enter 2nd color: ')
second =strInput

if first=="blue" and second=="red" or first=="red" and second=="blue":
    print('magenta')

elif first=="blue" and second=="green" or first=="green" and second=="blue":
    print('cyan')

elif first=="red" and second=="green" or first=="green" and second=="red":
    print('yellow') 

else:
    print('invalid input')
