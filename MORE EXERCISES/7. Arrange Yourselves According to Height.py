'''
7. Arrange Yourselves According to Height
'''

strInput=input('enter height of 1st person: ')
h1=float(strInput)
strInput=input('enter height of 1st person: ')
h2=float(strInput)
strInput=input('enter height of 1st person: ')
h3=float(strInput)

feet=3.28084
h1=h1*feet
h2=h2*feet
h3=h3*feet

if h1 <= h2 and h2 <= h3:
    print(h1,h2,h3)

elif h1 <= h3 and h3 <= h2:
    print(h1,h3,h2)

elif h2 <= h1 and h1 <= h3:
    print(h2,h1,h3)

elif h2 <= h3 and h3 <= h1:
    print(h2,h3,h1)

elif h3 <= h1 and h1 <= h2:
    print(h3,h1,h2)

elif h3 <= h2 and h2 <= h1:
    print(h3,h2,h1)
