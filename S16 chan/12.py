order = input("What's your order? (Fried Chicken/Burger Steak/Tapsilog) ")
kind = input("Ala carte or Value meal? ")

age = int(input("How old are you? "))

pay = float(input("How much did you pay? "))


if order == "Fried Chicken":
    if age >= 60:
        if kind == "Value meal":
            print("Your change is: ", pay - (85 * .8), "pesos")
        else:
            print("Your change is: ", pay - (75 * .8), "pesos")
    else:
        if kind == "Value meal":
            print("Your change is: ", pay - 85, "pesos")
        else:
            print("Your change is: ", pay - 75, "pesos")
elif order == "Burger Steak":
    if age >= 60:
        if kind == "Value meal":
            print("Your change is: ", pay - (50 * .8), "pesos")
        else:
            print("Your change is: ", pay - (40 * .8), "pesos")
    else:
        if kind == "Value meal":
            print("Your change is: ", pay - 50, "pesos")
        else:
            print("Your change is: ", pay - 40, "pesos")
else:
    if age >= 60:
        if kind == "Value meal":
            print("Your change is: ", pay - (70 * .8), "pesos")
        else:
            print("Your change is: ", pay - (60 * .8), "pesos")
    else:
        if kind == "Value meal":
            print("Your change is: ", pay - 70, "pesos")
        else:
            print("Your change is: ", pay - 60, "pesos")
