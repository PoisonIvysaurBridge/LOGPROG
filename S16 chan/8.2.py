year = int(input("Enter a year: "))

year = year % 4
year2 = year % 100
year3 = year % 400


if year == 0 and year3 == 0 or year2 == 0:
    print("It's a leap year!")
else:
    print("It's not a leap year.")
