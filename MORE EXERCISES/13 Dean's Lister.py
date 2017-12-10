'''
13. Dean's Lister
Assuming we only have three subjects in the term:
LOGPROG 3 units
INTR-IT 3 units
FITWELL 2 units
Write a program that accepts the grades of the student for each of those subjects, and then displays the
grade point average (GPA) of the student for the term. To compute for the GPA, multiply the grade for
each subject with the number of units to get the weighted grade for that subject. Add all the weighted
grades and then divide it by the total number of units to get the term GPA.
If the GPA of the student is at least 3.400, the program should display that the student is a rst honor
dean's lister. If the GPA of the student is at least 3.000 but less than 3.400, the program display that
the student is a second honor dean's lister.
'''

strInput=input('enter LOGPROG grade: ')
LOGPROG=float(strInput)
strInput=input('enter INTR-IT grade: ')
INTRIT=float(strInput)
strInput=input('enter FITWELL grade: ')
FITWELL=float(strInput)

units=LOGPROG*3 + INTRIT*3 + FITWELL *2
GPA= units/ 8
print ('Your GPA is',GPA)

if GPA >= 3.4:
    print("Fisrt Dean's Lister!")

elif GPA >= 3.0:
    print("Second Dean's Lister!")
    


