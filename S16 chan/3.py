ask = input("Would you like to convert (a) from meters to kilometers or (b) from kilometers to meters? (a/b) ")

if ask == "a":
    meters = float(input("What is the value in meters? "))
    kilometers = meters / 1000
    print(kilometers, "kilometers")
else:
    kilometers = float(input("What is the value in kilometers? "))
    meters = kilometers * 1000
    print(meters, "meters")
