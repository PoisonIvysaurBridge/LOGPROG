#hangman
#This code isnt free, you owe me 500 pesos >:[
ansr = input("Play (yes/no)?")
import random
while ansr != "no":
    loner = input("any:Single player or x:multi player?")
    level = 1
    ______ = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','1','2','3','4','5','6','7','8','9','0','.','/',',','\\',"'",'"',';',':',',','>','<','[',']','{','}','|','~','`','!','@','#','$','%','^','&','*','(',')','-','=','_','+','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    commandments = ['Chicken Wings', 'Skin', 'Boulevard', 'Angel', 'Geronimo', 'Christmas', 'Birthday', 'Tomorrow Land', 'Star','League of Legends', 'Hall of Fame', 'Donald Trump', 'DLSU', 'Frame', 'Motor Boat','Square Garden', 'The Script', 'Coldplay','Robocraft','Roblox','Star Wars','Macbook','Windows > OSX', 'Apple < Microsoft']
    _____________________ = "" #this is the thing
    done = []
    letrs = []
###################################################################################
    if loner == "x":
        _________ = input("Enter encrypted keyword:")
        ___________ = "_"
        __________=""
        _________________________ = ""
        _________________________________________________ = True
        _________________________________ = 0

        for _ in range(0, len(_________)):
            if _________[_] == "_":
                _________________________________ = _________________________________+1
            elif _________[_] == ".":
                _________________________ = _________________________+str(_________________________________)
                _________________________________ = 0
        for _ in range(0, len(_________________________)):
            if _ % 2 == 1:
                _____________________ = _____________________+______[int(_________________________[_-1]+_________________________[_])-1]
######################################################################################################

    
    else:
        _____________________ = random.choice(commandments)
    c = 1
    while c <= len(_____________________):
        if _____________________[c-1] == " ":
            pass
        else:
            if (_____________________[c-1].lower() in letrs)  == False:
                letrs.append(_____________________[c-1].lower())
        c+=1

        
    def makeScreen(level):##do this for leveling
        tip = ""
        c = 1
        while c <= len(_____________________):
            if _____________________[c-1] == " ":
                tip = tip+" "
            else:
                if (_____________________[c-1].lower() in done) == True:
                    tip = tip+_____________________[c-1]

                else:
                    tip = tip+"_"
            c+=1

        print("|----")
        if level == 8:
            print("|   X")
        elif level >=2:
            print("|   O")
        else:
            print("|   ")
        if level > 4:
            print("|  /|\\")
        elif level == 4:
            print("|  /|")
        elif level == 3:
            print("|   |")
        else:
            print("|")
        if level >= 3:
            print("|   |")
        else:
            print("|")
        if level >= 7:
            print("|  / \\")
        elif level == 6:
            print("|  / ")
        else:
            print("|")

        print(tip)
    def checkifDone(z):
        if z == ' ':
            return False
        else:
            if (z.lower() in done) == True:
                return False
            else:
                done.append(z.lower())
                return True

    def playGame():
        level = 1
        j=""
        while level <= 7 and len(letrs) > 0 and j != _____________________:
            print(level)
            makeScreen(level)
            j = input("Input a letter:")
            if checkifDone(j) == True:

                if (j.lower() in letrs) == True:
                    letrs.remove(j.lower())
                else:
                    level +=1
            else:
                print("Invalid input")

        makeScreen(level)
        if len(letrs) > 0 and j != _____________________:
            print("coorect word:"+ _____________________)
        else:
            print("You win!")
    playGame()
    ansr = input("Play (yes/no)?") 
