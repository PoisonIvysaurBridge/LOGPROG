'''
Exercise 2
Write a program that will display the corresponding grade point equivalent
(GPE) of a given nal grade. Assume that the passing score the course is
60 and the GPE is shown below.

Minimum Score GPE
0 0.0
60 1.0
66 1.5
72 2.0
78 2.5
83 3.0
89 3.5
94 4.0
S.
'''

strInput= input ("enter final grade: ")
GPE= float(strInput)

if GPE >= 60 and GPE < 66:
    GPE= 1.0
    print ("GPE is",GPE)

elif GPE >= 66 and GPE < 72:
    GPE= 2.0
    print ("GPE is",GPE)

elif GPE >= 72 and GPE < 78:
    GPE= 2.5
    print ("GPE is",GPE)

elif GPE >= 78 and GPE < 83:
    GPE= 3.0
    print ("GPE is",GPE)

elif GPE >= 83 and GPE < 89:
    GPE= 3.5
    print ("GPE is",GPE)

elif GPE >= 94:
    GPE= 4.0
    print ("GPE is",GPE)

else:
    GPE= 0.0
    print("GPE is",GPE)

