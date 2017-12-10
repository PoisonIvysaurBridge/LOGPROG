enter = int(input("Station number where you entered? (1-15) "))
exited = int(input("Station number where you exited? (1-15) "))

base = exited - enter
base = abs (base)

if base >= 1:
    if base <= 3:
        print("Fare: 20 pesos")
    else:
        base = (base - 3) * 2.50
        base = base + 20
        print("Fare:", base, "pesos")
else:
    print("Fare: 0 pesos")


