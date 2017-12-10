''' RUSH HOUR '''
'''
input the number of males and females in LRT, the train is divided into two parts
the normal section, and the female seciton.
the female section has a max of 10 while the normal section has a max of 30 seats.
the normal section can have both male and female passengers.
output the number of trains needed.'''

M=int(input("enter number of male passengers: "))
F=int(input("enter the number of female passengers: "))
T=M//20
if M%20 > 0:
    T=T+1
    F=F - (T*10 + 20-M%20)
    #print(T)
    #print(F)
    if F > 0:
        T2=F//30
        if F%30 > 0:
            T2=T2+1
        T=T+T2
            
elif M==0 and F > 0:
    F=F//30
    if F%30 > 0:
        T=T+1

print("number of trains needed:",T)
