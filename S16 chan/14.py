cm = int(input("What's the current month? (1-12) "))
cd = int(input("What's the current day? "))
cy = int(input("What's the current year? "))

bm = int(input("What's your birthday month? (1-12) "))
bd = int(input("Your birthday is on which day? "))
by = int(input("What's your birth year? "))

age = cy - by

if cm - bm < 0:
    print("You're", age - 1, "years old.")
elif cm - bm == 0:
    if cd - bd >= 0:
        print("You're", age, "years old.")
    else:
        print("You're", age - 1, "years old.")
else:
    print("You're", age, "years old.")
