'''
Exercise 1
Write a program that will compute for the user's year of birth, given the
current year and the age of the user. Assume that the user already
celebrated his birthday for the current year.In addition, the user will input
whether he has celebrated his birthday for the current year or not.
'''

strInput=input("enter current year: ")
year=int(strInput)


strInput=input("enter age: ")
age=int(strInput)

strInput=input("have you celebrated your birthday yet?(Yah/Nah): ")
ans=strInput

if ans=="Yah":
    birth=year-age
    print (birth)

elif ans=="Nah":
    birth= year- age - 1
    print(birth)
    
else:
    print("enter Yah or Nah")

