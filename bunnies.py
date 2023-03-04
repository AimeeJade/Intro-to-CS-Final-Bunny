from graphics import *
from math import *
from random import *
import time


def main():
    win = GraphWin("Bunny", 100, 100)
    win.setBackground("light cyan")
    win.setCoords(0, 0, 1000, 1000)
    xposition = [0, 1000/3, 2000/3, 1000]
    xp = choice(xposition)
    grass = Grass(xp)
    grass.grass.draw(win)
    
    #bunny -- all starting at x = 0 for now
    x = randrange(0, 1000)
    y = 10 * abs(40 * sin((3 * pi/1000) * x))
    bun = Bunny(x, y)
    bun.bun.draw(win)

    #fox
    a = randrange(0, 1000)
    b = 100
    fox = Foxy(a, b)
    fox.fox.draw(win)

    #eagle
    c = randrange(0, 1000)
    d = 400 * sin((1/90)* c + 18) + 500
    eagle = Eagle(c, d)
    eagle.eagle.draw(win)

    #direction initialization
    right = True
    right2 = True
    right3 = True
    
    while win.checkKey() != 'q': 
        dy = (18 * pi * cos((3*pi*x)/1000) *sin((3*pi*x)/1000))/(5 * abs(sin((3*pi*x)/1000)))
        dd = (140 * cos((c/90) + 18))/9
        #dy_opposite = 
        if bun.bun.getCenter().getX() >= xp - 5 and bun.bun.getCenter().getX() <= xp + 5:
            grass.grass.undraw()
            #use wait function until a certain condition happens?
            #pause and make a new one
            #grass.grass.draw(win)
        if fox.fox.getCenter().getX() >= x - 5 and fox.fox.getCenter().getX() <= x + 5:
            bun.bun.undraw()
        if eagle.eagle.getCenter().getX() >= a - 5 and eagle.eagle.getCenter().getX() <= a + 5:
            fox.fox.undraw()
        
        time.sleep(0.01)
        #bunny movement
        if x > 1000: #checking to change direction if the circle is out of bounds on either end
            x -= 20
            bun.bun.move(-20,dy)
            right = False
        elif x < 0:
            x += 20
            bun.bun.move(20,dy)
            right = True
        if right: #movement based on the direction given by "right" variable
            x += 5
            bun.bun.move(5,dy)
        else:
            x -= 5
            bun.bun.move(-5,dy)

        #fox movement
        if a > 1000:
            a -= 20
            fox.fox.move(-20,0)
            right2 = False
        elif a < 0:
            a += 20
            fox.fox.move(20,0)
            right2 = True
        if right2:
            a += 5
            fox.fox.move(5,0)
        else:
            a -= 5
            fox.fox.move(-5,0)

        #eagle movement
        if c > 1000:
            c -= 20
            eagle.eagle.move(c,dd)
            right3 = False
        elif a < 0:
            a += 20
            eagle.eagle.move(20,dd)
            right3 = True
        if right3:
            a += 5
            eagle.eagle.move(5,dd)
        else:
            a -= 5
            eagle.eagle.move(-5,dd)



#how to make grass and bunny simultanous
class Grass:
   def __init__(self, xp):
       self.xp = xp
       self.y = 0
       self.grass = Circle(Point(xp, self.y), 50)
       self.grass.setFill("lightgreen")

class Bunny:
   def __init__(self, x, y):
       #x = randrange(0, 1000)
       #y = 10 * abs(40 * sin((3 * pi/1000) * x))
       self.x = x
       self.y = y
       self.bun = Circle(Point(self.x, self.y), 50)
       self.bun.setFill("pink")

   def bun_move_right(self, dy):
       dx = 3
       self.dx = dx
       self.dx += 3
       self.dy = dy
       self.dy = (18 * pi * cos((3* pi * self.dx)/1000) * sin((3 * pi * self.dx)/1000))/(5 * abs(sin((3 * pi * self.dx)/1000)))
       self.bun.move(self.dx, self.dy)

class Foxy:
   def __init__(self, a, b):
       #x = randrange(0, 500)
       #y = 100
       self.a = a
       self.b = b
       self.fox = Circle(Point(self.a, self.b), 50)
       self.fox.setFill("coral")

class Eagle:
   def __init__(self, c, d):
       #x = randrange(0, 1000)
       #y = 400 * sin((1/900)*self.x + 18) + 500
       self.c = c
       self.d = d
       self.eagle = Circle(Point(self.c, self.d), 50)
       self.eagle.setFill("peru")

#    def Bunmovement(self, win):
#        while self.x <= 1000:
#            self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
#            bob = Circle(Point(self.x, self.y), 50)
#            bob.setFill("pink")
#            bob.draw(win)
#            self.x = self.x + 33/2
#            time.sleep(0.05)
#            bob.undraw()
#            if self.x > 1000:
#                break
          
#        while self.x > 0:
#            self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
#            bob = Circle(Point(self.x, self.y), 50)
#            bob.setFill("pink")
#            bob.draw(win)
#            self.x = self.x - 33/2
#            time.sleep(0.05)
#            bob.undraw()

#    def Foxmovement(self, win):
#        while self.x <= 1000:
#            self.y = 100
#            lily = Circle(Point(self.x, self.y), 50)
#            lily.setFill("coral")
#            lily.draw(win)
#            self.x = self.x + 33
#            time.sleep(0.05)
#            lily.undraw()
#            if self.x > 1000:
#                break
#        while self.x > 0:
#            self.y = 100
#            lily = Circle(Point(self.x, self.y), 50)
#            lily.setFill("coral")
#            lily.draw(win)
#            self.x = self.x - 33
#            time.sleep(0.05)
#            lily.undraw()

  
#    def Eagmovement(self, win):
#        while self.x <= 1000:
#            self.y = 400 * sin((1/900)*self.x + 18) + 500
#            joe = Circle(Point(self.x, self.y), 50)
#            joe.setFill("peru")
#            joe.draw(win)
#            self.x = self.x + 33/2
#            time.sleep(0.05)
#            joe.undraw()
#            if self.x > 1000:
#                break
          
#        while self.x > 0:
#            self.y = 400 * sin((1/900)*self.x + 18) + 500
#            joe = Circle(Point(self.x, self.y), 50)
#            joe.setFill("peru")
#            joe.draw(win)
#            self.x = self.x - 33/2
#            time.sleep(0.05)
#            joe.undraw()
main()

'''
from graphics import *
from math import *
from random import *
import time


def main():
    win = GraphWin("Bunny", 1000, 1000)
    win.setBackground("light cyan")
    win.setCoords(0, 0, 1000, 1000)
    ground = Ground()
    ground.ground.draw(win)
    xposition = [0, 1000/3, 2000/3, 1000]
    xp = choice(xposition)
    grass = Grass(xp)
    grass.grass.draw(win)
    
    #bunny 
    x = randrange(0, 1000)
    y = 10 * abs(40 * sin((3 * pi/1000) * x))
    bun = Bunny(x, y)
    bun.bun.draw(win)

    #fox
    a = randrange(0, 1000)
    b = 100
    fox = Foxy(a, b)
    fox.fox.draw(win)

    #eagle
    c = randrange(0, 1000)
    d = 400 * sin((1/90)* c + 18) + 505
    eagle = Eagle(c, d)
    eagle.eagle.draw(win)
    
    while win.checkKey() != 'q': 
        if bun.bun.getCenter().getX() >= xp - 5 and bun.bun.getCenter().getX() <= xp + 5:
            grass.grass.undraw()
            xp = choice(xposition)
            newgrass = Grass(xp)
            newgrass.grass.draw(win)
        if fox.fox.getCenter().getX() >= x - 5 and fox.fox.getCenter().getX() <= x + 5:
            bun.bun.undraw()
        if eagle.eagle.getCenter().getX() >= a - 5 and eagle.eagle.getCenter().getX() <= a + 5:
            fox.fox.undraw()
        
        bun.bun.getX() += 3
        dy = (18 * pi * cos((3*pi*x)/1000) *sin((3*pi*x)/1000))/(5 * abs(sin((3*pi*x)/1000)))
        bun.bun.move(3, dy)
        #bun.bun_move_right() -- tyring to figure this out
        a += 0.5
        db = 0
        fox.fox.move(a,db)
        c += 3
        dd = (140 * cos((c/90) + 18))/9
        eagle.eagle.move(5, dd)

#how to make grass and bunny simultanous
class Ground:
    def __init__(self):
        self.ground = Line(Point(0, 10), Point(1000, 10))
        self.ground.setOutline("lightgreen")
        self.ground.setWidth(20)

class Grass:
   def __init__(self, xp):
       self.xp = xp
       self.y = 0
       self.grass = Circle(Point(xp, self.y), 50)
       self.grass.setFill("lightgreen")
    

class Bunny:
   def __init__(self, x, y):
       #x = randrange(0, 1000)
       #y = 10 * abs(40 * sin((3 * pi/1000) * x))
       self.x = x
       self.y = y
       self.bun = Circle(Point(self.x, self.y), 50)
       self.bun.setFill("pink")

   def bun_move_right(self, dy):
       dx = 3
       self.dx = dx
       self.dx += 3
       self.dy = dy
       self.dy = (18 * pi * cos((3* pi * self.dx)/1000) * sin((3 * pi * self.dx)/1000))/(5 * abs(sin((3 * pi * self.dx)/1000)))
       self.bun.move(self.dx, self.dy)

class Foxy:
   def __init__(self, a, b):
       #x = randrange(0, 500)
       #y = 100
       self.a = a
       self.b = b
       self.fox = Circle(Point(self.a, self.b), 50)
       self.fox.setFill("coral")

class Eagle:
   def __init__(self, c, d):
       #x = randrange(0, 1000)
       #y = 400 * sin((1/900)*self.x + 18) + 500
       self.c = c
       self.d = d
       self.eagle = Circle(Point(self.c, self.d), 50)
       self.eagle.setFill("peru")


main()

IDEAS FOR HOW TO KEEP IT IN THE WINDOW

from graphics import *
from math import *
from random import *
import time

#fyuck
win = GraphWin("Bunny", 1000, 1000)
win.setBackground("light cyan")
win.setCoords(0, 0, 1000, 1000)

#external coordinate initialization
x = 900
y = 500
x2 = 900
y2 = 800

#circle initialization
circle = Circle(Point(x,y), 20)
circle2 = Circle(Point(x2, y2), 30)
circle.draw(win)
circle2.draw(win)

#direction initialization
right = True
right2 = True

#main while loop
while win.checkKey() != 'q': 
#circle 1 movement
    time.sleep(0.01)
    if x > 1000: #checking to change direction if the circle is out of bounds on either end
        x -= 20
        circle.move(-20,0)
        right = False
    elif x < 0:
        x += 20
        circle.move(20,0)
        right = True
    if right: #movement based on the direction given by "right" variable
        x += 5
        circle.move(5,0)
    else:
        x -= 5
        circle.move(-5,0)

#circle 2 movement
    if x2 > 1000:
        x2 -= 20
        circle2.move(-20,0)
        right2 = False
    elif x2 < 0:
        x2 += 20
        circle2.move(20,0)
        right2 = True
    if right2:
        x2 += 5
        circle2.move(10,0)
    else:
        x2 -= 5
        circle2.move(-10,0)

'''
