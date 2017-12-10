s1 = float(input("Length of the first side of the triangle: "))
s2 = float(input("Length of the second side of the triangle: "))
s3 = float(input("Length of the third side of the triangle: "))

if s1 == s2 and s2 == s3:
    print("Equilateral triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
