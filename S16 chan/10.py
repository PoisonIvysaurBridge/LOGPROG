sexa = input("What's the first person's sex? (M/F) ")
sexb = input("What's the second person's sex? (M/F) ")

agea = int(input("What's the first person's age? "))
ageb = int(input("What's the second person's age? "))

loca = input("What's the first person's location? (Philippines/USA) ")
locb = input("What's the second person's location? (Philippines/USA) ")

if agea < 18 or ageb < 18:
    print("Sorry, you guys can't get married.")
elif sexa == "M" and sexb == "M":
    if loca == "Philippines" or locb == "Philippines":
        print("Sorry, you guys can't get married.")
    else:
        print("You guys can get married!!")
elif sexa == "F" and sexb == "F":
    if loca == "Philippines" or locb == "Philippines":
        print("Sorry, you guys can't get married.")
    else:
        print("You guys can get married!!")
else:
    print("You guys can get married!!")


