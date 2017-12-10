'''
11. Triangle Classifier
Write a program that accepts the lengths of the three sides of a triangle in meters. The program should
classify it into one of the following:
Equilateral All three sides are of the same length.
Isosceles Exactly two sides are of the same length.
Scalene No two sides are of the same length.
Note that even though modern mathematical denitions of isosceles triangle state that it should have at
least two sides of the same length (thus making all equilateral triangles isosceles as well), we will follow
the classical denition of an isosceles triangle for the sake of this problem.
'''

strInput= input("enter side 1: ")
s1= float(strInput)
strInput= input("enter side 2: ")
s2= float(strInput)
strInput= input("enter side 3: ")
s3= float(strInput)

if s1 == s2 and s2 == s3 and s1 == s3:
    print('Equilateral Triangle')
    
elif s1 == s2 or s2 == s3 or s1 == s3:
    print('isosceles Triangle')

else:
    print('scalene triangle')
