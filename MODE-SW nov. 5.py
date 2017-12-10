four=0
five=0
one=0
three=int(input("Value: "))
one=three
two=1
while three > 0:
    if three < one:
        print("Invalid input")
    elif three == one:
        two+=1
    else:
        if two >= five:
            four=one
            five=two
        one=three
        two=1
    three=int(input("Value: "))
print("Four=",four,"Five=",five)
