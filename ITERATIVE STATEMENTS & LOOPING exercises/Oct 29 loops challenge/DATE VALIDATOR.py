#color testing
'''from colorama import colored
print (colored('hello', 'red'), colored('world', 'green'))'''

invalid=True
while invalid:
    date=int(input("date: "))
    M= date//1000000
    D= date//10000 %100
    Y= date%10000
    if M==2 and D <=28 or (M==2 and D <=29 and (Y%4==0 and Y%100!=0 or Y%400==0)):
        invalid=False
    elif (M==4 or M==6 or M==9 or M==11) and D<=30:
        invalid=False
    elif (M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12) and D<=31:
        invalid=False
print("You have entered a valid date.")
        
