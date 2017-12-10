'''
Write a program that will compute for the user's nal grade in
LOGPROG and display Pass or Fail. The passing grade for
LOGPROG is 60.000.
Activity Weight
Quiz 1 20%
Quiz 2 20%
Class Participation 20%
Project 20%
Final Exam 20%
S.
'''

strInput= input ("enter Quiz 1 grade: ")
Q1= float (strInput)

strInput= input ("enter Quiz 2 grade: ")
Q2= float (strInput)

strInput= input ("enter Class Participation grade: ")
CP= float(strInput)

strInput= input ("enter Project grade: ")
proj= float(strInput)

strInput= input ("enter Final Exam grade: ")
FE= float (strInput)

fGrade= Q1*0.2 + Q2*0.2 + CP*0.2 + proj*0.2 + FE*0.2

if fGrade  >= 60:
     print ("Pass")

else:
     print ("Fail")
