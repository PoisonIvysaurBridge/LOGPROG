one = float(input("What's the first person's height in meters? "))
two = float(input("What's the second person's height in meters? "))
three = float(input("What's the third person's height in meters? "))

one = one * 3.28084
two = two * 3.28084
three = three * 3.28084

if one <= two and two <= three:
    print(one, "feet", two, "feet", three, "feet")#123

elif one <= three and three <= two:
    print(one, "feet", three, "feet", two, "feet")#132
    
elif two <= one and one <= three:
    print(two, "feet", one, "feet", three, "feet")#213
    
elif two <= three and three <= one:
    print(two, "feet", three, "feet", one, "feet")#231

elif three <= two and two <= one:
    print(three, "feet", two, "feet", one, "feet")#321
    
elif one <= two and three <= one:
    print(three, "feet", one, "feet", two, "feet")#312
