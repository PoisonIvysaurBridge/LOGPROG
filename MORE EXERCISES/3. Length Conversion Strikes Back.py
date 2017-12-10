'''
3. Length Conversion Strikes Back
'''

strInput=input('convert from meters to kilometers or kilometers to meters?(A/B) ')
ans=strInput

if ans=="A":
    strInput=input('enter meters:')
    meter=float(strInput)
    km=meter/1000
    print(km,'kilometers')

elif ans=="B":
    strInput=input('enter kilometer(s):')
    km=float(strInput)
    meter=km*1000
    print(meter,'meter(s)')

else:
    print('invalid input')
