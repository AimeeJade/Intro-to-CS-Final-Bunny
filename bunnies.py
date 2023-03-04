from graphics import *
from math import *
from random import *
import time


def main():
    win = GraphWin("Bunny", 1000, 1000)
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
    
    while win.checkKey() != 'q': 
        if bun.bun.getCenter().getX() >= xp - 5 and bun.bun.getCenter().getX() <= xp + 5:
            grass.grass.undraw()
            #pause and make a new one
            #grass.grass.draw(win)
        if fox.fox.getCenter().getX() >= x - 5 and fox.fox.getCenter().getX() <= x + 5:
            bun.bun.undraw()
        if eagle.eagle.getCenter().getX() >= a - 5 and eagle.eagle.getCenter().getX() <= a + 5:
            fox.fox.undraw()
        
        x += 3
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
        
        x += 3
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
'''
