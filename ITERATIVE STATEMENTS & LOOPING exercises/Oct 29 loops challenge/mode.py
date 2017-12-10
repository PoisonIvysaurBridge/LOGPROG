mode=0
maxTimes=0
curVal=0
n=int(input("n: "))
curVal=n
curTimes=1
while n > 0:
    n=int(input("n: "))
    if n < curVal:
        print ("Invalid input.")
    elif n== curVal:
        curTimes+=1
    else:
        if curTimes > maxTimes:
            maxTimes= curTimes
            mode= curVal
        curVal = n
        curTimes = 1
    
print("mode:",mode,maxTimes,"times")
