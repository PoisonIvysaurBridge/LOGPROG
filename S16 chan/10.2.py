sexa = input("What's the first person's sex? (M/F) ")
sexb = input("What's the second person's sex? (M/F) ")

agea = int(input("What's the first person's age? "))
ageb = int(input("What's the second person's age? "))

loc = input("What's their location? (Philippines/USA) ")

if agea >= 18 or ageb >= 18:
    if loc == "USA":
        print("They can get married!!")
    else:
        if sexa == sexb:
            print("Sorry, they can't get married.")
        else:
            print("They can get married!!")
else:
    print("Sorry, they can't get married.")
