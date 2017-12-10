length = int(input("What's the length of the rectangle? "))
width = int(input("What's the width of the rectangle? "))

ask = input("Would you like to compute for (a) the area or (b) the perimeter? (a/b) ")

if ask == "a":
    print("The rectangle's area is", length * width, "square meters.")
else:
    print("The rectangle's perimeter is", 2 * length + 2 * width, "meters.")
