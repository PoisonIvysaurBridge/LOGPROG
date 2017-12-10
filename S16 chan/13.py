log = float(input("LOGPROG grade: "))
it = float(input("INTR-IT grade: "))
fit = float(input("FITWELL grade: "))

log = log * 3
it = it * 3
fit = fit * 2
gpa = (log + it + fit) / 8

print("Your GPA is", gpa)

if gpa >= 3.400:
    print("You're a first honor dean's lister!")
elif gpa < 3.400 and gpa >= 3.000:
    print("You're a second honor dean's lister!")
