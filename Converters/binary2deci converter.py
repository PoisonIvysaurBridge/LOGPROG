###############################################
def binary2deci(binaryN):
    powerOf2=1
    deciConvert=0
    while binaryN > 0:
        binary = binaryN%10
        binaryN//=10
        deciConvert+=binary*powerOf2
        powerOf2*=2
    return(deciConvert)
# SAMPLE x=binary2deci(11100000)
# SAMPLE print(x)
###############################################

binaryN=int(input("binary number: "))
powerOf2=1
deciConvert=0
while binaryN > 0:
        binary = binaryN%10
        binaryN//=10
        deciConvert+=binary*powerOf2
        powerOf2*=2
print(deciConvert)
