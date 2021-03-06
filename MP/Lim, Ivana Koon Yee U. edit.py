'''BEHOLD THE AWESOME MACHINE PROJECT 
Poing of Sales System'''
############
# Task: Menu Prices & Initial Invetory & Main Menu
# Description: Built-in Menu items and their respective prices & Initial Inventory Stock
# Variables Used: cont, Option, Beef, Chix, regFries, LFries, regSoda, LSoda, regBeefC, LBeefC, regChixC, LChixC, IBB, IBP, ICP, IRF, ILF, IBW, IRSC, ILSC
# Outputs: Main Menu options; User input for options
############
''' Ala Carte Items '''
Beef= 80
Chix= 70
regFries= 20
LFries= 30
regSoda= 15
LSoda= 20

''' Combo Items '''
regBeefC= 100
LBeefC= 110
regChixC= 90
LChixC= 100

''' INVENTORY '''
IBB=0 # Burger Bun
IBP=0 # Beef Burger Patty
ICP=0 # Chicken Burger Patty
IRF=0 # Regular Fries
ILF=0 # Large Fries
IBW=0 # Burger Wrap
IRSC=0 # Regular Soda Cup
ILSC=0 # Large Soda Cup

''' END DAY INITIALIZATIONS '''
customer=0
totalSale=0 # for END DAY
cntA=0
cntB=0
cntC=0
cntD=0
cntE=0
cntF=0
cntG=0
cntH=0
cntI=0
cntJ=0

cont=True
while cont:
    print('\n------------ MAIN MENU ------------')
    print('1. Setup\n2. Start Day\n3. Exit\n')
    Option=int(input('Please choose an option (1, 2, or 3): '))
    
############
# Task: Setup
# Description: allows user to edit price of items in menu then displays summary & go back to main menu option
# Variables Used: cont, Option, ans, Beef, Chix, regFries, LFries, regSoda, LSoda, regBeefC, LBeefC, regChixC, LChixC
# Outputs: User input for price of each menu item and go back to main menu option; Summary of Menu with updated Price
############
    if Option==1:
        print('\n------------ Setup ------------')
        print('\n','*'*30,'MENU','*'*30)#print a table of the Menu
        print('_'*70,'\nAla Carte Items\t\t\tCombo Items\n'+'_'*70)
        print('Beef Burger\t\t',Beef,'\tBeef Burger Regular Combo\t',regBeefC,'\nChickent Burger\t\t',Chix,'\tBeef Burger Large Combo\t\t',LBeefC,'\nRegular Fries\t\t',regFries,'\tChicken Burger Regular Combo\t',regChixC,'\nLarge Fries\t\t',LFries,'\tChicken Burger Regular Combo\t',LChixC,'\nRegular Soda\t\t',regSoda,'\nLarge Soda\t\t',LSoda,'\n'+'_'*70)
        print('\n','-'*13,'MENU ITEM PRICE EDIT','-'*13)
        print('***** Ala Carte Items *****')
        Beef=float(input('enter price for Beef Burger: '))
        Chix=float(input('enter price for Chicken Burger: '))
        regFries=float(input('enter price for Regular Fries: '))
        LFries=float(input('enter price for Large Fries: '))
        regSoda=float(input('enter price for Regular Soda: '))
        LSoda=float(input('enter price for Large Soda: '))

        print('\n***** Combo Items *****')
        regBeefC= float(input('enter price for Beef Burger Regular Combo: '))
        LBeefC= float(input('enter price for Beef Burger Large Combo: '))
        regChixC= float(input('enter price for Chicken Burger Regular Combo: '))
        LChixC= float(input('enter price for Chicken Burger Large Combo: '))
        print('-'*50,'\n')

        print('='*12,'Summary of Menu','='*12)
        print('ALA CARTE ITEMS\t\t\tPRICE')
        print('Beef burger\t\t\tP'+str(Beef),'\nChicken burger\t\t\tP'+str(Chix),'\nRegular Fries\t\t\tP'+str(regFries),'\nLarge Fries\t\t\tP'+str(LFries),'\nRegular Soda\t\t\tP'+str(regSoda),'\nLarge Soda\t\t\tP'+str(LSoda)+'\n')
       
        print('COMBO\t\t\t\tPRICE')
        print('Beef Burger Regular Combo\tP'+str(regBeefC),'\nBeef Burger Large Combo\t\tP'+str(LBeefC),'\nChicken Burger Regular Combo\tP'+str(regChixC),'\nChicken Burger Large Combo\tP'+str(LChixC))
        print('='*42,'\n')

        ans=input('Go Back to MAIN MENU? (Yah/Nah): ')
        if ans=='Nah':
            cont=False
            print('Have a good day!')

############
# Task: Start Day--Restock & View Inventory
# Description: Restock allows user to add items in inventory; View Inventory displays the items in inventory and their Qty
# Variables Used: cont, Option, ReturnSD, SD, IBB, IBP, ICP, IRF, ILF, IBW, IRSC, ILSC
# Outputs:User input for restocking of items; View Inventory and the quantity remaining for each item 
############
    elif Option==2:
        '''cont=False'''
        ReturnSD=True
        while ReturnSD:
            print('\n------------ Start Day ------------')
            print('1. Restock\n2. View Inventory\n3. Accept Order\n4. End Day\n')
            SD=int(input('Please choose and option (1, 2, 3, or 4): '))
            if SD==1:
                print('\n============ Restock Inventory ============')
                curIBB= int(input('Enter BURGER BUN Qty: '))
                curIBP= int(input('Enter BEEF BURGER PATTY Qty: '))
                curICP= int(input('Enter CHICKEN BURGER PATTY Qty: '))
                curIRF= int(input('Enter REGULAR FRIES Qty: '))
                curILF= int(input('Enter LARGE FRIES Qty: '))
                curIBW= int(input('Enter BURGER WRAP Qty: '))
                curIRSC= int(input('Enter REGULAR SODA CUP Qty: '))
                curILSC= int(input('Enter LARGE SODA CUP Qty: '))
                IBB+=curIBB
                IBP+=curIBP
                ICP+=curICP
                IRF+=curIRF
                ILF+=curILF
                IBW+=curIBW
                IRSC+=curIRSC
                ILSC+=curILSC

            elif SD==2:
                print('\n============ View Inventory ============')
                print('ITEMS\t\t\tQUANTITY')
                print('Burger Bun\t\t',IBB,'\nBeef burger Patty\t',IBP,'\nChicken burger Patty\t',ICP,'\nRegular Fries\t\t',IRF,'\nLarge Fries\t\t',ILF,'\nBurger Wrap\t\t',IBW,'\nRegular Soda Cup\t',IRSC,'\nLarge Soda Cup\t\t',ILSC)
                print('========================================\n')

############
# Task: Start Day--Accept Order
# Description: 
# Variables Used: cont,Option,ReturnSD,SD, IBB,IBP,ICP,IRF,ILF,IBW,IRSC,ILSC, totalSale, cntA to cntJ, sumA to sumJ, QtyA to QtyJ
# Outputs: 
############
            elif SD==3:
                print('\n============ ACCEPT ORDER ============')
                accept=True
                more=True
                while accept: # new customer
                    sumA=0
                    sumB=0
                    sumC=0
                    sumD=0
                    sumE=0
                    sumF=0
                    sumG=0
                    sumH=0
                    sumI=0
                    sumJ=0

                    QtyA=0
                    QtyB=0
                    QtyC=0
                    QtyD=0
                    QtyE=0
                    QtyF=0
                    QtyG=0
                    QtyH=0
                    QtyI=0
                    QtyJ=0
                    print('\n','*'*30,'MENU','*'*30)#print a table of the Menu
                    print('_'*70,'\nAla Carte Items\t\t\tCombo Items\n'+'_'*70)
                    print('A) Beef Burger\t\t',Beef,'\tG) Beef Burger Regular Combo\t',regBeefC,'\nB) Chickent Burger\t',Chix,'\tH) Beef Burger Large Combo\t',LBeefC,'\nC) Regular Fries\t',regFries,'\tI) Chicken Burger Regular Combo\t',regChixC,'\nD) Large Fries\t\t',LFries,'\tJ) Chicken Burger Regular Combo\t',LChixC,'\nE) Regular Soda\t\t',regSoda,'\nF) Large Soda\t\t',LSoda,'\n'+'_'*70)
                    print('\n------------ NEW ORDER --------------')
                    while more: # more order
                        strOrder=input('Enter Order Choice: ')
                        strOrder=strOrder.upper()
                        
                        if strOrder == 'X' or strOrder == 'x': # esc button proceed with receipt
                             more=False
                        elif not (strOrder=="A" or strOrder=="B" or strOrder=="C" or strOrder=="D" or strOrder=="E" or strOrder=="F" or strOrder=="G" or strOrder=="H" or strOrder=="I" or strOrder=="J"):
                            print("INVALID INPUT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        else:
                            more=True
                            Qty=int(input('Enter Quantity: '))
                             
                            if strOrder=='A': # Beef
                                if IBB>0 and IBB >= Qty and IBP>0 and IBP >= Qty and IBW>0 and IBW>= Qty:
                                    QtyA=Qty
                                    sumA=Qty*Beef
                                    IBB-=1*Qty
                                    IBP-=1*Qty
                                    IBW-=1*Qty
                                    cntA+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='B': # Chix
                                if IBB>0 and IBB>= Qty and ICP>0 and ICP>=Qty and IBW>0 and IBW>=Qty:
                                    QtyB=Qty
                                    sumB=Qty*Chix
                                    IBB-=1*Qty
                                    ICP-=1*Qty
                                    IBW-=1*Qty
                                    cntB+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='C': # regFries
                                if IRF>0 and IRF>=Qty:
                                    QtyC=Qty
                                    sumC=Qty*regFries
                                    IRF-=1*Qty
                                    cntC+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='D': # LFries
                                if ILF>0 and ILF>=Qty:
                                    QtyD=Qty
                                    sumD=Qty*LFries
                                    ILF-=1*Qty
                                    cntD+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='E': # regSoda
                                if IRSC>0 and IRSC>=Qty:
                                    QtyE=Qty
                                    sumE=Qty*regSoda
                                    IRSC-=1*Qty
                                    cntE+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='F': # LSoda
                                if ILSC>0 and ILSC>=Qty:
                                    QtyF=Qty
                                    sumF=Qty*LSoda
                                    ILSC-=1*Qty
                                    cntF+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='G': # regBeefC
                                if IBB>0 and IBB>=Qty and IBP>0 and IBP>=Qty and IRF>0 and IRF>=Qty and IBW>0 and IBW>=Qty and IRSC>0 and IRSC>=Qty:
                                    QtyG=Qty
                                    sumG=Qty*regBeefC
                                    IBB-=1*Qty
                                    IBP-=1*Qty
                                    IBW-=1*Qty
                                    IRF-=1*Qty
                                    IRSC-=1*Qty
                                    cntG+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='H': #LBeefC
                                if IBB>0 and IBB>=Qty and IBP>0 and IBP>=Qty and ILF>0 and ILF>=Qty and IBW>0 and IBW>=Qty and ILSC>0 and ILSC>=Qty:
                                    QtyH=Qty
                                    sumH=Qty*LBeefC
                                    IBB-=1*Qty
                                    IBP-=1*Qty
                                    IBW-=1*Qty
                                    ILF-=1*Qty
                                    ILSC-=1*Qty
                                    cntH+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='I': #regChixC
                                if IBB>0 and IBB>=Qty and ICP>0 and ICP>=Qty and IRF>0 and IRF>=Qty and IBW>0 and IBW>=Qty and IRSC>0 and IRSC>=Qty:
                                    QtyI=Qty
                                    sumI=Qty*regChixC
                                    IBB-=1*Qty
                                    ICP-=1*Qty
                                    IBW-=1*Qty
                                    IRF-=1*Qty
                                    IRSC-=1*Qty
                                    cntI+=1*Qty
                                else:
                                    print("not enough stock")
                            elif strOrder=='J': #LChixC
                                if IBB>0 and IBB>=Qty and ICP>0 and ICP>=Qty and ILF>0 and ILF>=Qty and IBW>0  and IBW>=Qty  and ILSC>0 and ILSC>=Qty:
                                    QtyJ=Qty
                                    sumJ=Qty*LChixC
                                    IBB-=1*Qty
                                    ICP-=1*Qty
                                    IBW-=1*Qty
                                    ILF-=1*Qty
                                    ILSC-=1*Qty
                                    cntJ+=1*Qty
                                else:
                                    print("not enough stock")
                            else:
                                print('invalid input')
                        
                        '''willOrderMORE=input('More Order?(Y/N): ')   #asks user if the customer still wants to order more
                        if willOrderMORE=='N' or willOrderMORE=='n':#if the customer doesn't want anymore orders,                                                                                               
                            more=False                              #the sys will exit the[more]loop & proceed with the rest of the[accept]loop   
                            print()'''
                        
                    customer+=1
                    #if strOrder != 'X' or strOrder != 'x': #'''if IBB>0 and IBP>0 and ICP>0 and IRF>0 and ILF>0 and IBW>0 and IRSC>0 and ILSC>0: #checks Inventory first before proceeding to receipt'''
                        
                    #Generation of customer's receipt
                    print('='*40)
                    print('CUSTOMER #',customer,'\n')
                    
                    if QtyA != 0:
                        print(QtyA,'Beef Burger -> P',sumA)
                    if QtyB != 0:
                        print(QtyB,'Chicken Burger -> P',sumB)
                    if QtyC != 0:
                        print(QtyC,'Regular Fries -> P',sumC)
                    if QtyD != 0:
                        print(QtyD,'Large Fries -> P',sumD)
                    if QtyE != 0:
                        print(QtyE,'Regular Soda -> P',sumE)
                    if QtyF != 0:
                        print(QtyF,'Large Soda -> P',sumF)
                    if QtyG != 0:
                        print(QtyG,'Beef Burger Regular Combo -> P',sumG)
                    if QtyH != 0:
                        print(QtyH,'Beef Burger Large Combo -> P',sumH)
                    if QtyI != 0:
                        print(QtyI,'Chicken Burger Regular Combo -> P',sumI)
                    if QtyJ != 0:
                        print(QtyJ,'Chicken Burger Large Combo -> P',sumJ)
                    Total=sumA + sumB + sumC + sumD + sumE + sumF + sumG + sumH + sumI + sumJ
                    totalSale+=Total
                    print('\nTotal amount:\t\t\tP'+str(Total))
                    amtPaid=float(input('\nAmount received:\t\tP'))
                    if amtPaid < Total:
                        print("lacking:", Total-amtPaid)
                    else:
                        print('Change:\t\t\t\tP'+str(amtPaid-Total))
                    print('\nThank You! Please See Us Again! :)\nThis serves as your OFFICIAL RECEIPT\n'+'='*40+'\n')

                    '''returnSD=input('Return to Start Day?(Y/N): ')#asks user if the sys will go back to start day or proceed with the next customer([accept]loop)
                        if returnSD=='Y' or returnSD=='y': #if the user wants to exit to start day, then the sys will exit[accept]loop & go to start day menu
                            accept=False
                        more=True
                        else:
                        print("OH NO IT'S THE END OF THE WORLD THERE'S NOT ENOUGH INVENTORY PLS RESTOCK IMMEDIATELY") 
                        accept=False'''
                        
                        
                    accept=False
            elif SD==4: #End Day
                ReturnSD=False #will not go back to start menu anymore
                print('\n','='*20,' Day-end Report ','='*20)
                print('\nTotal Customers:',customer,)
                print('\nSales:\n')
                print('Item\t\t\t\tQty\tU-Price\t\tAmt')
                print('Beef Burger\t\t\t',cntA,'\t',Beef,'\t\t', cntA*Beef)
                print('Chicken Burger\t\t\t',cntB,'\t',Chix,'\t\t',cntB*Chix )
                print('Regular Fries\t\t\t',cntC,'\t',regFries,'\t\t',cntC*regFries)
                print('Large Fries\t\t\t',cntD,'\t',LFries,'\t\t',cntD*LFries)
                print('Regular Soda\t\t\t',cntE,'\t',regSoda,'\t\t',cntE*regSoda )
                print('Large Soda\t\t\t',cntF,'\t',LSoda,'\t\t',cntF*LSoda )
                print('Beef Burger Regular Combo\t',cntG,'\t',regBeefC,'\t\t',cntG*regBeefC)
                print('Beef Burger Large Combo\t\t',cntH,'\t',LBeefC,'\t\t',cntH*LBeefC )
                print('Chicken Burger Regular Combo\t',cntI,'\t',regChixC,'\t\t',cntI*regChixC)
                print('Chicken Burger Large Combo\t',cntJ,'\t',LChixC,'\t\t',cntJ*LChixC )

                print('\n\nTotal Sale:\t\tP'+str(totalSale))
                print('\nFinal Inventory:\n')
                print('Burger Bun\t\t',IBB,'\nBeef burger Patty\t',IBP,'\nChicken burger Patty\t',ICP,'\nRegular Fries\t\t',IRF,'\nLarge Fries\t\t',ILF,'\nBurger Wrap\t\t',IBW,'\nRegular Soda Cup\t',IRSC,'\nLarge Soda Cup\t\t',ILSC)
                print('='*60,'\nHave a nice day! :) YESHHHH LOGPROG IS AWESOME')
    elif Option==3: # Exit
        cont=False
        print('Have a nice day! :) LOGPROG IS AWESOME')
    else:
        print('invalid input!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
import time # I did this for cmd viewing
time.sleep(999)
        
        
        



        
        
    

   
    
    
    
