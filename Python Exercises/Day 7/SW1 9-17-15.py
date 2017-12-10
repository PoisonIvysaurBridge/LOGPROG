'''
Write a program that will compute for the user's year of birth, given
the current year and the age of the user. Assume that the user
already celebrated his birthday for the current year.
'''


strInput=input("enter current year: ")
year=int(strInput)


strInput=input("enter age: ")
age=int(strInput)

birth=year-age
print (birth)
