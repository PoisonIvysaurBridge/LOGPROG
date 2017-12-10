###############
# This is to certify that this project is my own work, based on my personal
# efforts in studying and applying the concepts learned. I have constructed
# the functions and their respective algorithms and corresponding code by
# myself. The program was run,tested, and debugged by my own efforts. I
# further certify that I have not copied in part or whole or otherwise
# plagiarized the work of other students and/or persons.
#
# ________________
# Aldrich Limheya, 11427167
################
#######################
#Task: Input stocks 
#Description: This segment lets the cashier type the stock for the day
#Variables Used: BurgerBun,BeefBurgerPatty,ChickenBurgerPatty,RegularFries,LargeFries,
#BurgerWrap,RegularSodaCup,LargeSodaCup
#Outputs: The stock available for the day
#######################
BurgerBun=int(input("Enter Burger Buns in stock today"))
BeefBurgerPatty=int(input("Enter Beef Burger Patties in stock today"))
ChickenBurgerPatty=int(input("Enter Chicken Burger Patty in stock today"))
RegularFries=int(input("Enter Regular Fries in stock today"))
LargeFries=int(input("Enter Large Fries in stock today"))
BurgerWrap=int(input("Enter Burger Wrap in stock today"))
RegularSodaCup=int(input("Enter Regular Soda Cup in stock today"))
LargeSodaCup=int(input("Enter Large Soda Cup in stock today"))
print ("")
#######################
#Task: Stores the price of each product
#Description: The variables here have a value which is their price
#Variables Used: BB,CB.RF,LF,LS,RS,BBRC,BBLC,CBLC,CBRC
#Outputs: At the end of the day report, it outputs the price of each product 
#######################
BB=80
CB=70
RF=20
LF=30
RS=15
LS=20
BBRC=100
BBLC=110
CBRC=90
CBLC=100
######################
#Task: The variables here are for storing the amount of products sold
#Description: Every product in the menu starts at zero and as it is being sold,
#the amount of products adds up and shows at the end of the day report
#Variables Used: BEEFBURGER,CHICKENBURGER,REGULARFRIES,LARGEFRIES,REGULARSODA,
#LARGESODA,BEEFBURGERREGCOMBO,BEEFBURGERLARGCOMBO,CHICKENBURGERREGCOMBO,CHICKENBURGERLARGCOMBO
#Outputs: At the end of the day report, the amount of the products sold will be displayed. 
######################
BEEFBURGER=0
CHICKENBURGER=0
REGULARFRIES=0
LARGEFRIES=0
REGULARSODA=0
LARGESODA=0
BEEFBURGERREGCOMBO=0
BEEFBURGERLARGCOMBO=0
CHICKENBURGERREGCOMBO=0
CHICKENBURGERLARGCOMBO=0
######################
#Task: Storing the sum of the price of the ordered products and customer count.
#Description: The variable for customer is for stating the amount of customers who bought something.
#The variable for A is for the sum of the price of all the food ordered on the first order. another variable is assigned
#if there are more orders.
#Variables Used: customer,A
#Outputs: shown at the receipt for the customer and A is for either the total bill of a customer for 1 order only or,
#for adding it to the total price if it is with the second order or more orders.
#######################
customer=0
A=0
#######################
#Task: Getting the total stock and inputing if there is a customer or not
#Description: All of the stock is added and if the total stock is zero, the end of the day report will be displayed.
#countercustomer is also for inputting if there is a customer, it will continue the program if not then it will display
#the end of the day report.
#Variables Used: TotalStock,countercustomer 
#Outputs:if there is no stock or if there is no customers for the day, end of the day report will be displayed or else,
#it will continue the program 
#######################
TotalStock=BurgerBun+BeefBurgerPatty+ChickenBurgerPatty+RegularFries+LargeFries+BurgerWrap+RegularSodaCup+LargeSodaCup
countercustomer=input("Enter y if there is a customer. if none, press any key and click enter=)")
while countercustomer=="y" and TotalStock>0:
    QTY=0
    NQTY=0
    PQ1=0
    A=0
    PQ=0
#######################
#Task: Getting the order and how many orders
#Description: This determines the order and how many orders will there be
#Variables Used: Order,QTY
#Outputs: How many orders a customer orders and the orders itself
#######################
    Order=input("Please enter the order of your customer")
    QTY=int(input("How many orders?"))
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product
#whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,BurgerBun,BeefBurgerPatty,BurgerWrap,PQ1,BEEFBURGER
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    if Order=="BB":
        if BurgerBun>=QTY and BeefBurgerPatty>=QTY and BurgerWrap>=QTY:
            print(QTY,"Beef Burger-",(BB*QTY))
            BurgerBun=BurgerBun-QTY
            BeefBurgerPatty=BeefBurgerPatty-QTY
            BurgerWrap=BurgerWrap-QTY
            if BurgerBun>=0 and BeefBurgerPatty>=0 and BurgerWrap>=0:
                PQ1=(BB*QTY)
                BEEFBURGER=BEEFBURGER+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers that is available with the stock given.")
                print ("Burger Bun:",BurgerBun+QTY)
                print ("Beef Burger Patty:",BeefBurgerPatty+QTY)
                print ("Burger Wrap:",BurgerWrap+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers that is available with the stock given.")
            print ("Burger Bun:",BurgerBun)
            print ("Beef Burger Patty:",BeefBurgerPatty)
            print ("Burger Wrap:",BurgerWrap)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product whenever
#a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program continues
#, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again because
#it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the first
#order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,BurgerBun,ChickenBurgerPatty,BurgerWrap,PQ1,CHICKENBURGER
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="CB":
        if BurgerBun>=QTY and ChickenBurgerPatty>=QTY and BurgerWrap>=QTY:
            print(QTY,"Chicken Burger-",(CB*QTY))
            BurgerBun=BurgerBun-QTY
            ChickenBurgerPatty=ChickenBurgerPatty-QTY
            BurgerWrap=BurgerWrap-QTY
            if BurgerBun>=0 and ChickenBurgerPatty>=0 and BurgerWrap>=0:
                PQ1=(CB*QTY)
                CHICKENBURGER=CHICKENBURGER+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burgers that is available with the stock given.")
                print ("Burger Bun:",BurgerBun+QTY)
                print ("Chicken Burger Patty:",BeefBurgerPatty+QTY)
                print ("Burger Wrap:",BurgerWrap+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burgers that is available with the stock given.")
            print ("Burger Bun:",BurgerBun)
            print ("Chicken Burger Patty:",BeefBurgerPatty)
            print ("Burger Wrap:",BurgerWrap)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product whenever a
# product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program continues
#, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again because
#it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the first
#order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,RegularFries,PQ1,REGULARFRIES
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="RF":
        if RegularFries>=QTY:
            print(QTY,"Regular Fries-",(RF*QTY))
            RegularFries=RegularFries-QTY
            if RegularFries>=0:
                PQ1=(RF*QTY)
                REGULARFRIES=REGULARFRIES+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Fries that is available with the stock given.")
                print ("Regular Fries:",RegularFries+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Fries that is available with the stock given.")
            print ("Regular Fries:",RegularFries)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product whenever
#a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program continues,
#it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again because
#it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the first
#order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,LARGEFRIES,PQ1,LargeFries
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="LF":
        if LargeFries>=QTY:
            print(QTY,"Large Fries-",(LF*QTY))
            LargeFries=LargeFries-QTY
            if LargeFries>=0:
                PQ1=(LF*QTY)
                LARGEFRIES=LARGEFRIES+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Fries that is available with the stock given.")
                print ("Large Fries:",LargeFries+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Fries that is available with the stock given.")
            print ("Large Fries:",LargeFries)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product whenever
#a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program continues,
#it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again because
#it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the first
#order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,REGULARSODA,PQ1,RegularSoda
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="RS":
        if RegularSodaCup>=QTY:
            print(QTY,"Regular Soda-",(RS*QTY))
            RegularSodaCup=RegularSodaCup-QTY
            if RegularSodaCup>=0:
                PQ1=(RS*QTY)
                REGULARSODA=REGULARSODA+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Soda that is available with the stock given.")
                print ("Regular Soda Cup:",RegularSodaCup+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Soda that is available with the stock given.")
            print ("Regular Soda Cup:",RegularSodaCup)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product whenever
#a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program continues,
#it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again because
#it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the first
#order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,LargeSoda,PQ1,LARGESODA
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="LS":
        if LargeSodaCup>=QTY:
            print(QTY,"Large Soda-",(LS*QTY))
            LargeSodaCup=LargeSodaCup-QTY
            if LargeSodaCup>=0:
                PQ1=(LS*QTY)
                LARGESODA=LARGESODA+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Soda that is available with the stock given.")
                print ("Large Soda Cup:",LargeSodaCup+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Soda that is available with the stock given.")
            print ("Large Soda Cup:",LargeSodaCup)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product whenever
#a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,BurgerBun,BeefBurgerPatty,BurgerWrap,RegularSodaCup,RegularFries,PQ1,BEEFBURGERREGCOMBO
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="BBRC":
        if RegularSodaCup>=QTY and RegularFries>=QTY and BurgerBun>=QTY and BeefBurgerPatty>=QTY and BurgerWrap>=QTY:
            print(QTY,"Beef Burger Regular Combo-",(BBRC*QTY))
            BurgerBun=BurgerBun-QTY
            BeefBurgerPatty=BeefBurgerPatty-QTY
            BurgerWrap=BurgerWrap-QTY
            RegularFries=RegularFries-QTY
            RegularSodaCup=RegularSodaCup-QTY
            if RegularSodaCup>=0 and RegularFries>=0 and BurgerBun>=0 and BeefBurgerPatty>=0 and BurgerWrap>=0:
                PQ1=(BBRC*QTY)
                BEEFBURGERREGCOMBO=BEEFBURGERREGCOMBO+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burger Regular Combo that is available with the stock given.")
                print ("Burger Bun:",BurgerBun+QTY)
                print ("Beef Burger Patty:",BeefBurgerPatty+QTY)
                print ("Burger Wrap:",BurgerWrap+QTY)
                print ("Regular Soda Cup:",RegularSodaCup+QTY)
                print ("Regular Fries:",RegularFries+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burger Regular Combo that is available with the stock given.")
            print ("Burger Bun:",BurgerBun)
            print ("Beef Burger Patty:",BeefBurgerPatty)
            print ("Burger Wrap:",BurgerWrap)
            print ("Regular Soda Cup:",RegularSodaCup)
            print ("Regular Fries:",RegularFries)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product
#whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,BurgerBun,BeefBurgerPatty,LargeFries,LargeSodaCup,BEEFBURGERLARGCOMBO,BurgerWrap,PQ1
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="BBLC":
        if LargeSodaCup>=QTY and LargeFries>=QTY and BurgerBun>=QTY and BeefBurgerPatty>=QTY and BurgerWrap>=QTY:
            print(QTY,"Beef Burger Large Combo-",(BBLC*QTY))
            BurgerBun=BurgerBun-QTY
            BeefBurgerPatty=BeefBurgerPatty-QTY
            BurgerWrap=BurgerWrap-QTY
            LargeFries=LargeFries-QTY
            LargeSodaCup=LargeSodaCup-QTY
            if LargeSodaCup>=0 and LargeFries>=0 and BurgerBun>=0 and BeefBurgerPatty>=0 and BurgerWrap>=0:
                PQ1=(BBLC*QTY)
                BEEFBURGERLARGCOMBO=BEEFBURGERLARGCOMBO+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burger Large Combo that is available with the stock given.")
                print ("Burger Bun:",BurgerBun+QTY)
                print ("Beef Burger Patty:",BeefBurgerPatty+QTY)
                print ("Burger Wrap:",BurgerWrap+QTY)
                print ("Large Soda Cup:",LargeSodaCup+QTY)
                print ("Large Fries:",LargeFries+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burger Large Combo that is available with the stock given.")
            print ("Burger Bun:",BurgerBun)
            print ("Beef Burger Patty:",BeefBurgerPatty)
            print ("Burger Wrap:",BurgerWrap)
            print ("Large Soda Cup:",LargeSodaCup)
            print ("Large Fries:",LargeFries)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product
#whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,BurgerBun,RegularFries,RegularSodaCup,ChickenBurgerPatty,CHICKENBURGERREGCOMBO,BurgerWrap,PQ1
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="CBRC":
        if RegularSodaCup>=QTY and RegularFries>=QTY and BurgerBun>=QTY and ChickenBurgerPatty>=QTY and BurgerWrap>=QTY:
            print(QTY,"Chicken Burger Regular Combo-",(CBRC*QTY))
            BurgerBun=BurgerBun-QTY
            ChickenBurgerPatty=ChickenBurgerPatty-QTY
            BurgerWrap=BurgerWrap-QTY
            RegularFries=RegularFries-QTY
            RegularSodaCup=RegularSodaCup-QTY
            if RegularSodaCup>=0 and RegularFries>=0 and BurgerBun>=0 and ChickenBurgerPatty>=0 and BurgerWrap>=0:
                PQ1=(CBRC*QTY)
                CHICKENBURGERREGCOMBO=CHICKENBURGERREGCOMBO+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chioken Burger Regular Combo that is available with the stock given.")
                print ("Burger Bun:",BurgerBun+QTY)
                print ("Chicken Burger Patty:",ChickenBurgerPatty+QTY)
                print ("Burger Wrap:",BurgerWrap+QTY)
                print ("Regular Soda Cup:",RegularSodaCup+QTY)
                print ("Regular Fries:",RegularFries+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chioken Burger Regular Combo that is available with the stock given.")
            print ("Burger Bun:",BurgerBun)
            print ("Chicken Burger Patty:",ChickenBurgerPatty)
            print ("Burger Wrap:",BurgerWrap)
            print ("Regular Soda Cup:",RegularSodaCup)
            print ("Regular Fries:",RegularFries)
#######################
#Task: Computes the total price for the quantity and the product product price and decrease the stock that makes up the product
#whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.    
#Variables Used: Order,QTY,BurgerBun,CHICKENBURGERLARGCOMBO,LargeFries,LargeSodaCup,BeefBurgerPatty,BurgerWrap,PQ1,BEEFBURGER
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
    elif Order=="CBLC":
        if LargeSodaCup>=QTY and LargeFries>=QTY and BurgerBun>=QTY and ChickenPatty>=QTY and BurgerWrap>=QTY:
            print(QTY,"Chicken Burger Large Combo-",(CBLC*QTY))
            BurgerBun=BurgerBun-QTY
            ChickenBurgerPatty=ChickenBurgerPatty-QTY
            BurgerWrap=BurgerWrap-QTY
            LargeFries=LargeFries-QTY
            LargeSodaCup=LargeSodaCup-QTY
            if LargeSodaCup>=0 and LargeFries>=0 and BurgerBun>=0 and ChickenPatty>=0 and BurgerWrap>=0:
                PQ1=(CBLC*QTY)
                CHICKENBURGERLARGCOMBO=CHICKENBURGERLARGCOMBO+QTY
            else:
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burger Large Burger that is available with the stock given.")
                print ("Burger Bun:",BurgerBun+QTY)
                print ("Chicken Burger Patty:",ChickenBurgerPatty+QTY)
                print ("Burger Wrap:",BurgerWrap+QTY)
                print ("Large Soda Cup:",LargeSodaCup+QTY)
                print ("Large Fries:",LargeFries+QTY)
        else:
            print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burger Large Burger that is available with the stock given.")
            print ("Burger Bun:",BurgerBun)
            print ("Chicken Burger Patty:",ChickenBurgerPatty)
            print ("Burger Wrap:",BurgerWrap)
            print ("Large Soda Cup:",LargeSodaCup)
            print ("Large Fries:",LargeFries)
#######################
#Task: Getting the next order or multiple orders for the same customer
#Description: You will input if the same customer has another order or not
#Variables Used: MoreOrder
#Outputs: Another order or the end of the day report
#######################    
    MoreOrder=input("Is there another order for the same customer? Type Y if yes or N if no")
    while MoreOrder=="Y" or MoreOrder=="y":
#######################
#Task: Getting the order and how many orders the second time
#Description: This determines the second or more orders and how many orders will there be
#Variables Used: Order2,NQTY
#Outputs: How many orders a customer orders and the orders itself
#######################
        Order2=input("Please enter the additional order of your customer")
        NQTY=int(input("How many orders?"))
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that
#makes up the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,BurgerBun,BeefBurgerPatty,BurgerWrap,PQ1,BEEFBURGER
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        if Order2=="BB":
            if BurgerBun>=NQTY and BeefBurgerPatty>=NQTY and BurgerWrap>=NQTY:
                print(NQTY,"Beef Burger-",(BB*NQTY))
                BurgerBun=BurgerBun-NQTY
                BeefBurgerPatty=BeefBurgerPatty-NQTY
                BurgerWrap=BurgerWrap-NQTY
                if BurgerBun>=0 and BeefBurgerPatty>=0 and BurgerWrap>=0:
                    PQ=(BB*NQTY)
                    BEEFBURGER=BEEFBURGER+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers that is available with the stock given.")
                    print ("Burger Bun:",BurgerBun+NQTY)
                    print ("Beef Burger Patty:",BeefBurgerPatty+NQTY)
                    print ("Burger Wrap:",BurgerWrap+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers that is available with the stock given.")
                print ("Burger Bun:",BurgerBun)
                print ("Beef Burger Patty:",BeefBurgerPatty)
                print ("Burger Wrap:",BurgerWrap)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes
#up the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,BurgerBun,ChickenBurgerPatty,BurgerWrap,PQ1,CHICKENBURGER
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="CB":
            if BurgerBun>=NQTY and ChickenBurgerPatty>=NQTY and BurgerWrap>=NQTY:
                print(NQTY,"Chicken Burger-",(CB*NQTY))
                BurgerBun=BurgerBun-NQTY
                ChickenBurgerPatty=ChickenBurgerPatty-NQTY
                BurgerWrap=BurgerWrap-NQTY
                if BurgerBun>=0 and ChickenBurgerPatty>=0 and BurgerWrap>=0:
                    PQ=(CB*NQTY)
                    CHICKENBURGER=CHICKENBURGER+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of CHicken Burgers that is available with the stock given.")
                    print ("Burger Bun:",BurgerBun+NQTY)
                    print ("Chicken Burger Patty:",ChickenBurgerPatty+NQTY)
                    print ("Burger Wrap:",BurgerWrap+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of CHicken Burgers that is available with the stock given.")
                print ("Burger Bun:",BurgerBun)
                print ("Chicken Burger Patty:",ChickenBurgerPatty)
                print ("Burger Wrap:",BurgerWrap)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes
#up the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,RegularFries,PQ1,REGULARFRIES
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="RF":
            if RegularFries>=NQTY:
                print(NQTY,"Regular Fries-",(RF*NQTY))
                RegularFries=RegularFries-NQTY
                if RegularFries>=0:
                    PQ=(RF*NQTY)
                    REGULARFRIES=REGULARFRIES+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Fries that is available with the stock given.")
                    print ("Regular Fries:",RegularFries+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Fries that is available with the stock given.")
                print ("Regular Fries:",RegularFries)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes up
#the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,LARGEFRIES,PQ1,LargeFries
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="LF":
            if LargeFries>=NQTY:
                print(NQTY,"Large Fries-",(LF*NQTY))
                LargeFries=LargeFries-NQTY
                if LargeFries>=0:
                    PQ=(LF*NQTY)
                    LARGEFRIES=LARGEFRIES+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Fries that is available with the stock given.")
                    print ("Large Fries:",LargeFries+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Fries that is available with the stock given.")
                print ("Large Fries:",LargeFries)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes
#up the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,REGULARSODA,PQ1,RegularSoda
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="RS":
            if RegularSodaCup>=NQTY:
                print(NQTY,"Regular Soda-",(RS*NQTY))
                RegularSodaCup=RegularSodaCup-NQTY
                if RegularSodaCup>=0:
                    PQ=(RS*NQTY)
                    REGULARSODA=REGULARSODA+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Soda that is available with the stock given.")
                    print ("Regular Soda Cup:",RegularSodaCup+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Regular Soda that is available with the stock given.")
                print ("Regular Soda Cup:",RegularSodaCup)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes up
#the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,LargeSoda,PQ1,LARGESODA
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="LS":
            if LargeSodaCup>=NQTY:
                print(NQTY,"Large Soda-",(LS*NQTY))
                LargeSodaCup=LargeSodaCup-NQTY
                if LargeSodaCup>=0:
                    PQ=(LS*NQTY)
                    LARGESODA=LARGESODA+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Soda that is available with the stock given.")
                    print ("Large Soda Cup:",LargeSodaCup+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Large Soda that is available with the stock given.")
                print ("Large Soda Cup:",LargeSodaCup)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes up
#the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,BurgerBun,BeefBurgerPatty,BurgerWrap,RegularSodaCup,RegularFries,PQ1,BEEFBURGERREGCOMBO
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="BBRC":
            if RegularSodaCup>=NQTY and RegularFries>=NQTY and BurgerBun>=NQTY and BeefBurgerPatty>=NQTY and BurgerWrap>=NQTY:
                print(NQTY,"Beef Burger Regular Combo-",(BBRC*NQTY))
                BeefBurgerPatty=BeefBurgerPatty-NQTY
                BurgerWrap=BurgerWrap-NQTY
                BurgerBun=BurgerBun-NQTY
                RegularFries=RegularFries-NQTY
                RegularSodaCup=RegularSodaCup-NQTY
                if RegularSodaCup>=0 and RegularFries>=0 and BurgerBun>=0 and BeefBurgerPatty>=0 and BurgerWrap>=0:
                    PQ=(BBRC*NQTY)
                    BEEFBURGERREGCOMBO=BEEFBURGERREGCOMBO+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers Regular Combo that is available with the stock given.")
                    print ("Burger Bun:",BurgerBun+NQTY)
                    print ("Beef Burger Patty:",BeefBurgerPatty+NQTY)
                    print ("Burger Wrap:",BurgerWrap+NQTY)
                    print ("Regular Soda Cup:",RegularSodaCup+NQTY)
                    print ("Regular Fries:",RegularFries+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers Regular Combo that is available with the stock given.")
                print ("Burger Bun:",BurgerBun)
                print ("Beef Burger Patty:",BeefBurgerPatty)
                print ("Burger Wrap:",BurgerWrap)
                print ("Regular Soda Cup:",RegularSodaCup)
                print ("Regular Fries:",RegularFries)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes up
#the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,BurgerBun,BeefBurgerPatty,LargeFries,LargeSodaCup,BEEFBURGERLARGCOMBO,BurgerWrap,PQ1
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="BBLC":
            if LargeSodaCup>=NQTY and LargeFries>=NQTY and BurgerBun>=NQTY and BeefBurgerPatty>=NQTY and BurgerWrap>=NQTY:
                print(NQTY,"Beef Burger Large Combo-",(BBLC*NQTY))
                BurgerBun=BurgerBun-NQTY
                BeefBurgerPatty=BeefBurgerPatty-NQTY
                BurgerWrap=BurgerWrap-NQTY
                LargeFries=LargeFries-NQTY
                LargeSodaCup=LargeSodaCup-NQTY
                if LargeSodaCup>=0 and LargeFries>=0 and BurgerBun>=0 and BeefBurgerPatty>=0 and BurgerWrap>=0:
                    PQ=(BBLC*NQTY)
                    BEEFBURGERLARGCOMBO=BEEFBURGERLARGCOMBO+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers Large Combo that is available with the stock given.")
                    print ("Burger Bun:",BurgerBun+NQTY)
                    print ("Beef Burger Patty:",BeefBurgerPatty+NQTY)
                    print ("Burger Wrap:",BurgerWrap+NQTY)
                    print ("Large Soda Cup:",LargeSodaCup+NQTY)
                    print ("Large Fries:",LargeFries+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Beef Burgers Large Combo that is available with the stock given.")
                print ("Burger Bun:",BurgerBun)
                print ("Beef Burger Patty:",BeefBurgerPatty)
                print ("Burger Wrap:",BurgerWrap)
                print ("Large Soda Cup:",LargeSodaCup)
                print ("Large Fries:",LargeFries)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes up
#the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,BurgerBun,RegularFries,RegularSodaCup,ChickenBurgerPatty,CHICKENBURGERREGCOMBO,BurgerWrap,PQ1
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="CBRC":
            if RegularSodaCup>=NQTY and RegularFries>=NQTY and BurgerBun>=NQTY and ChickenBurgerPatty>=NQTY and BurgerWrap>=NQTY:
                print(NQTY,"Chicken Burger Regular Combo-",(CBRC*NQTY))
                BurgerBun=BurgerBun-NQTY
                ChickenBurgerPatty=ChickenBurgerPatty-NQTY
                BurgerWrap=BurgerWrap-NQTY
                RegularFries=RegularFries-NQTY
                RegularSodaCup=RegularSodaCup-NQTY
                if RegularSodaCup>=0 and RegularFries>=0 and BurgerBun>=0 and ChickenBurgerPatty>=0 and BurgerWrap>=0:
                    PQ=(CBRC*NQTY)
                    CHICKENBURGERREGCOMBO=CHICKENBURGERREGCOMBO+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burger Regular Combo that is available with the stock given.") 
                    print ("Burger Bun:",BurgerBun+NQTY)
                    print ("Chicken Burger Patty:",ChickenBurgerPatty+NQTY)
                    print ("Burger Wrap:",BurgerWrap+NQTY)
                    print ("Regular Soda Cup:",RegularSodaCup+NQTY)
                    print ("Regular Fries:",RegularFries+NQTY)
            else:
                PQ=0
                print ("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burger Regular Combo that is available with the stock given.") 
                print ("Burger Bun:",BurgerBun)
                print ("Chicken Burger Patty:",ChickenBurgerPatty)
                print ("Burger Wrap:",BurgerWrap)
                print ("Regular Soda Cup:",RegularSodaCup)
                print ("Regular Fries:",RegularFries)
#######################
#Task: Computes the total price of multiple orders for the quantity and the product product price and decrease the stock that makes up
#the product whenever a product is sold and adds
#the number of products will increase and display at the end of the day report for the number of a certain product is sold.
#Description: If the order is a beef burger then it will continue the program or tell that there is no more stock. If the program
#continues, it wll get the total price of the order
#and subtract the quantity of the stock and if the stock is less than zero, it will display the remaining stock by adding it again
#because it was first subtracted so when you add it again,
#it will display the original stocks before subtracting it. If not, the total price will be stored and added to A as the sum of the
#first order and add the number of the product sold in the first order.
#and in the end if there is another order, it will ask again
#Variables Used: Order,NQTY,BurgerBun,CHICKENBURGERLARGCOMBO,LargeFries,LargeSodaCup,BeefBurgerPatty,BurgerWrap,PQ1,BEEFBURGER
#Outputs: Either the remaining stock or the order will be processed and be stored to another variable at the end
#######################
        elif Order2=="CBLC":
            if LargeSodaCup>=NQTY and LargeFries>=NQTY and BurgerBun>=NQTY and ChickenBurgerPatty>=NQTY and BurgerWrap>=NQTY:
                print(NQTY,"Chicken Burger Large Combo-",(CBLC*NQTY))
                BurgerBun=BurgerBun-NQTY
                ChickenBurgerPatty=ChickenBurgerPatty-NQTY
                BurgerWrap=BurgerWrap-NQTY
                LargeFries=LargeFries-NQTY
                LargeSodaCup=LargeSodaCup-NQTY
                if LargeSodaCup>=0 and LargeFries>=0 and BurgerBun>=0 and ChickenBurgerPatty>=0 and BurgerWrap>=0:
                    PQ=(CBLC*NQTY)
                    CHICKENBURGERLARGCOMBO=CHICKENBURGERLARGCOMBO+NQTY
                else:
                    PQ=0
                    print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burger Large Combo that is available with the stock given.")
                    print ("Burger Bun:",BurgerBun+NQTY)
                    print ("Chicken Burger Patty:",ChickenBurgerPatty+NQTY)
                    print ("Burger Wrap:",BurgerWrap+NQTY)
                    print ("Large Soda Cup:",LargeSodaCup+NQTY)
                    print ("Large Fries:",LargeFries+NQTY)
            else:
                PQ=0
                print("Here is the remaining amount of stocks. Please enter the appropriate amount of Chicken Burger Large Combo that is available with the stock given.")
                print ("Burger Bun:",BurgerBun)
                print ("Chicken Burger Patty:",ChickenBurgerPatty)
                print ("Burger Wrap:",BurgerWrap)
                print ("Large Soda Cup:",LargeSodaCup)
                print ("Large Fries:",LargeFries)
#######################
#Task: Adds the first order Total price to A and determining if there is another customer
#Description: The PQ is the first order and it adds to A to store how much A has and then adds to the total price when there is a problem.
#Variables Used: A,PQ,MoreOrder
#Outputs: At the end of the if program to get the receipt, it will add to the Total price.
#######################
        A=A+PQ
        MoreOrder=input("Is there another order for the same customer? Type Y if yes or N if no")
        print ("")
#######################
#Task: Getting the Total Price and adding 1 to customer or be equal to itself if there is no actual order
#Description: This adds PQ1 and the Total price and determines whether there is a customer or not
#Variables Used: TotalPrice,A,PQ1,customer 
#Outputs: Displays the customer amount
#######################
    TotalPrice=A+PQ1
    if TotalPrice==0:
        customer==customer
    else:
        customer=customer+1
    print ("Customer",customer)    
    print("Total amount:",TotalPrice)
#######################
#Task: This will process the payment
#Description: When the Total price is greater than zero, the program will process the payment and ask for the payment.
#if you pay less than the total price, you will enter again the correct amount or it will continue the prohram and get the change
#If there is another customer, the program will repeat taking the next customer 
#Variables Used: TotalPrice,AmountPay,Change,countercustomer
#Outputs: How much you paid and the change
#######################
    if TotalPrice>0:
        AmountPay=int(input("Amount Received:"))
        while AmountPay<TotalPrice:
            AmountPay=int(input("Enter again Amount Received:"))
        Change=AmountPay-TotalPrice
        print ("Change:", Change)
    print("")
    countercustomer=input("Enter y if there is a customer. if none, press any key and click enter=)")
#######################
#Task: The variables here are for storing the amount of the total price of the products sold
#Description: Each variable is multiplied by its original price and will store each of the total price of the products
#Variables Used: D,E,F,G,H,I,J,K,L,M,BB,CB,RF,LF,LS,RS,BBRC,BBLC,CBRC,CBLC,BEEFBURGER,CHICKENBURGER,REGULARFRIES,REGULARSODA,
#LARGESODA,LARGEFRIES,BEEFBURGERREGCOMBO,
#BEEFBURGERLARGCOMBO,CHICKENBURGERREGCOMBO,CHICKENBURGERLARGCOMBO
#Outputs: It will output at the end of the day report and will display how much of a product was sold
#######################
D=BB*BEEFBURGER
E=CB*CHICKENBURGER
F=RF*REGULARFRIES
G=LF*LARGEFRIES
H=RS*REGULARSODA
I=LS*LARGESODA
J=BBRC*BEEFBURGERREGCOMBO
K=BBLC*BEEFBURGERLARGCOMBO
L=CBRC*CHICKENBURGERREGCOMBO
M=CBLC*CHICKENBURGERLARGCOMBO
#######################
#Task: Displaying the end of the day report for each product sold, the price of the product and the total product price and
#displays the number of customers that paid for the day.
#Description: Displaying the number of products sold and it adds up as the loop program is taking place. it also displays the
#computed total price of each products.
#Variables Used: D,E,F,G,H,I,J,K,L,M,BB,CB,RF,LF,LS,RS,BBRC,BBLC,CBRC,CBLC,BEEFBURGER,CHICKENBURGER,REGULARFRIES,REGULARSODA,
#LARGESODA,LARGEFRIES,BEEFBURGERREGCOMBO,
#BEEFBURGERLARGCOMBO,CHICKENBURGERREGCOMBO,CHICKENBURGERLARGCOMBO,TPA
#Outputs: Number of products sold, their price and their Total price for each product
#######################
TPA=D+E+F+G+H+I+J+K+L+M
print ("DAY END REPORT")
print ("TOTAL CUSTOMERS:",customer)
print ("Sales")
print ("Beef Burger sold:",BEEFBURGER,"                        ","P",BB,"     ",(D)  )
print ("Chicken Burger sold:",CHICKENBURGER,"                     ","P",CB,"     ",(E))
print ("Regular Fries sold:",REGULARFRIES,"                      ","P",RF,"     ",(F))
print ("Large Fries sold:",LARGEFRIES,"                        ","P",LF,"     ",(G))
print ("Regular Soda sold:",REGULARSODA,"                       ","P",RS,"     ",(H))
print ("Large Soda sold:",LARGESODA,"                         ","P",LS ,"     ",(I))
print ("Beef Burger Regular Combo sold:",BEEFBURGERREGCOMBO,"         ","P",BBRC,"     ",(J))
print ("Beef burger Large Combo sold:",BEEFBURGERLARGCOMBO,"           ","P",BBLC,"     ",(K))
print ("Chicken burger Regular Combo sold:",CHICKENBURGERREGCOMBO,"       ","P",CBRC,"     ",(L))
print ("Chicken burger Large Combo sold:",CHICKENBURGERLARGCOMBO,"        ","P",CBLC,"     ",(M))
#######################
#Task: Display the Total Sale and the Final Inventory
#Description: The final inventory will be displayed because it was subtracted from the original inventory. every time a product is sold
#Variables Used: BurgerBun,BeefBurgerPatty,ChickenBurgerPatty,RegularFries,LargeFries,
#BurgerWrap,RegularSodaCup,LargeSodaCup
#Outputs: Display the Total Sale and the Final Inventory
#######################
print ("Total Sale:",TPA)
print ("Final Inventory:")
print ("Burger Bun:","                    ",BurgerBun)
print ("Beef Burger Patty:","             ",BeefBurgerPatty)
print ("Chicken Burger Patty:","          ",ChickenBurgerPatty)
print ("Regular Soda Cup:","              ",RegularSodaCup)
print ("Large Soda Cup:","                ",LargeSodaCup)
print ("Regular Fries","                  ",RegularFries)
print ("Large Fries","                    ",LargeFries)
print ("Burger Wrap:","                   ",BurgerWrap)
