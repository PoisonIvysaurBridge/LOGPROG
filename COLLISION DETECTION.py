''' COLLISION DETECTION '''
ULX1=int(input("enter 1st upper left X coordinate: "))
ULY1=int(input("enter 1st upper left Y coordinate: "))
LRX1=int(input("enter 1st Lower right X coordinate: "))
LRY1=int(input("enter 1st Lower right Y coordinate: "))
ULX2=int(input("enter 2nd upper left X coordinate: "))
ULY2=int(input("enter 2nd upper left Y coordinate: "))
LRX2=int(input("enter 2nd Lower right X coordinate: "))
LRY2=int(input("enter 2nd Lower right Y coordinate: "))

if (ULX1 < ULX2 or ULX1 > LRX2) and (LRX1 < ULX2 or LRX1 > LRX2) or (ULY1 < ULY2 or ULY1 > LRY2) and (LRY1 < ULY2 or LRY1 > LRY2):
    print("no collision")
#elif (ULX1 < ULX2 or ULX1 > LRX2) and (LRX1 < ULX2 or LRX1 > LRX2) 
else:
    print("COLLISION DETECTED!")
