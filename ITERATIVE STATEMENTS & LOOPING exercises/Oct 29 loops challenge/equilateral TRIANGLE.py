# without fill ###################################################### 1
n=int(input('n: '))
copy=n
k=1
while k<=n:
    j=1
    while j<= n:
        if j>= copy:
            if j==copy or j==n or k==1 or k==n:
                print('*0',end='')
            else:
                print('88',end='')
        else:
            print('0',end='')
        j+=1
    copy-=1
    print()
    k+=1
    
# with fill ######################################################## 2
n=int(input('n: '))
copy=n
k=1
while k<=n:
    j=1
    while j<= n:
        if j>= copy and j<= n:
            print('*0',end='')
        else:
            print('0',end='')
        j+=1
    copy-=1
    print()
    k+=1
    
# upside down ##################################################### 3
n=int(input('n: '))
copy=1
k=1
while k <= n:
    j=1
    while j <= n:
        if j >= copy:
            if j==copy or j==n:
                print('*0',end='')
            else:
                print('88',end='')
        else:
            print('0',end='')
        j+=1
    copy+=1
    print()
    k+=1

# diamond ######################################################### 4
n=int(input('n: '))
copy=n
k=1
while k<=n:
    j=1
    while j<= n:
        if j>= copy:
            if j==copy or j==n:
                print('*0',end='')
            else:
                print('88',end='')
        else:
            print('0',end='')
        j+=1
    copy-=1
    print()
    k+=1

copy2=1
k2=1
while k2 <= n:
    j2=1
    while j2 <= n:
        if j2 >= copy2 and j2 <= n:
            if j2==copy2 or j2==n:
                print('*0',end='')
            else:
                print('88',end='')
        else:
            print('0',end='')
        j2+=1
    copy2+=1
    print()
    k2+=1

# hourglass ###################################################### 5
print()
n=int(input('n: '))
copy2=1
k2=1
while k2 <= n:
    j2=1
    while j2 <= n:
        if j2 >= copy2 and j2 <= n:
            if j2==copy2 or j2==n or k2==1 or k2==n:
                print('*0',end='')
            else:
                print('88',end='')
        else:
            print('0',end='')
        j2+=1
    copy2+=1
    print()
    k2+=1
    

copy=n
k=1
while k<=n:
    j=1
    while j<= n:
        if j>= copy:
            if j==copy or j==n or k==1 or k==n:
                print('*0',end='')
            else:
                print('00',end='')
        else:
            print(' ',end='')
        j+=1
    copy-=1
    print()
    k+=1
    
''' ######### CODE OF MISS    #############################################'''
# upside down triangle
print()
print('CODE OF MISS')

n=int(input('n: '))
copy=1
k=1
while k <= n:
    j=1
    while j <= 2*n:
        if j==k or j+k== 2*n:
            print('*0',end="")
        else:
            print("0",end='')
        j+=1
    copy+=1
    k+=1
    print()

import turtle
# colormixer

from turtle import Screen, Turtle, mainloop

class ColorTurtle(Turtle):

    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("turtle")
        self.resizemode("user")
        self.shapesize(3,3,5)
        self.pensize(10)
        self._color = [0,0,0]
        self.x = x
        self._color[x] = y
        self.color(self._color)
        self.speed(0)
        self.left(90)
        self.pu()
        self.goto(x,0)
        self.pd()
        self.sety(1)
        self.pu()
        self.sety(y)
        self.pencolor("gray25")
        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0,min(y,1)))
        self._color[self.x] = self.ycor()
        self.fillcolor(self._color)
        setbgcolor()

def setbgcolor():
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())

def main():
    global screen, red, green, blue
    screen = Screen()
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)

    red = ColorTurtle(0, .5)
    green = ColorTurtle(1, .5)
    blue = ColorTurtle(2, .5)
    setbgcolor()

    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1,1.15)
    writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()



