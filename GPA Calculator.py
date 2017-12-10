# gpa calcu
print("========== WELCOME TO THE GPA CALCULATOR! LET'S GET THAT GPA RIGHT! ==========")
print("\nNOTE: Do not include non-academic courses in the number of courses\n"+"*"*80)
n=int(input("\nenter the number of courses: "))
units=0
totUnits=0
while n> 0:
    grade= float(input("enter grade of a course: "))
    nUnits= float(input("enter course units: "))
    units+= nUnits
    totUnits+= grade* nUnits
    n-=1
gpa= totUnits/ units
print("\ntotal weight:",totUnits)
print("total units:",units)
print("term gpa:", gpa)
