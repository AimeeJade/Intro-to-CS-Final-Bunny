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
    Grass_instance = Grass(win, xp)
    
    #bunny
    x = 0
    y = 0
    bob = Circle(Point(x, y), 50)
    bob.setFill("pink")
    bob.draw(win)

    #fox
    a = 0
    b = 100
    lily = Circle(Point(a, b), 50)
    lily.setFill("coral")
    lily.draw(win)

    #eagle
    c = 0
    d = 199.605
    joe = Circle(Point(c, d), 50)
    joe.setFill("peru")
    joe.draw(win)
    
    while bob.getCenter().getX() <= 1000: 
        x += 3
        dy = (18 * pi * cos((3*pi*x)/1000) *sin((3*pi*x)/1000))/(5 * abs(sin((3*pi*x)/1000)))
        bob.move(3, dy)
        a += 0.5
        db = 0
        lily.move(a,db)
        c += 3
        dd = (140 * cos((c/90) + 18))/9
        joe.move(5, dd)

    while win.checkKey() != 'q':
        pass


#how to make grass and bunny simultanous
class Grass:
   def __init__(self, win, xp):
       self.xp = xp
       self.y = 0
       self.grass = Circle(Point(xp, self.y), 50)
       self.grass.setFill("lightgreen")
       self.grass.draw(win)

class Bunny:
   def __init__(self, win, x, y):
       x = randrange(0, 1000)
       y = 10 * abs(40 * sin((3 * pi/1000) * x))
       self.x = x
       self.y = y
       bob = Circle(Point(self.x, self.y), 50)
       bob.setFill("pink")
       bob.draw(win)
  
   def Bunmovement(self, win):
       while self.x <= 1000:
           self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
           bob = Circle(Point(self.x, self.y), 50)
           bob.setFill("pink")
           bob.draw(win)
           self.x = self.x + 33/2
           time.sleep(0.05)
           bob.undraw()
           if self.x > 1000:
               break
          
       while self.x > 0:
           self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
           bob = Circle(Point(self.x, self.y), 50)
           bob.setFill("pink")
           bob.draw(win)
           self.x = self.x - 33/2
           time.sleep(0.05)
           bob.undraw()
          


class Foxy:
   def __init__(self, win, x):
       x = randrange(0, 500)
       y = 100
       self.x = x
       self.y = y
       lily = Circle(Point(self.x, self.y), 50)
       lily.setFill("coral")
       lily.draw(win)

   def Foxmovement(self, win):
       while self.x <= 1000:
           self.y = 100
           lily = Circle(Point(self.x, self.y), 50)
           lily.setFill("coral")
           lily.draw(win)
           self.x = self.x + 33
           time.sleep(0.05)
           lily.undraw()
           if self.x > 1000:
               break
       while self.x > 0:
           self.y = 100
           lily = Circle(Point(self.x, self.y), 50)
           lily.setFill("coral")
           lily.draw(win)
           self.x = self.x - 33
           time.sleep(0.05)
           lily.undraw()

class Eagle:
   def __init__(self, win, x, y):
       x = randrange(0, 1000)
       y = 400 * sin((1/900)*self.x + 18) + 500
       self.x = x
       self.y = y
       joe = Circle(Point(self.x, self.y), 50)
       joe.setFill("peru")
       joe.draw(win)

  
   def Eagmovement(self, win):
       while self.x <= 1000:
           self.y = 400 * sin((1/900)*self.x + 18) + 500
           joe = Circle(Point(self.x, self.y), 50)
           joe.setFill("peru")
           joe.draw(win)
           self.x = self.x + 33/2
           time.sleep(0.05)
           joe.undraw()
           if self.x > 1000:
               break
          
       while self.x > 0:
           self.y = 400 * sin((1/900)*self.x + 18) + 500
           joe = Circle(Point(self.x, self.y), 50)
           joe.setFill("peru")
           joe.draw(win)
           self.x = self.x - 33/2
           time.sleep(0.05)
           joe.undraw()
main()

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
    Grass_instance = Grass(win, xp)
    
    #bunny
    x = 0
    y = 0
    bob = Circle(Point(x, y), 50)
    bob.setFill("pink")
    bob.draw(win)

    #fox
    a = 0
    b = 100
    lily = Circle(Point(a, b), 50)
    lily.setFill("coral")
    lily.draw(win)

    #eagle
    c = 0
    d = 199.605
    joe = Circle(Point(c, d), 50)
    joe.setFill("peru")
    joe.draw(win)
    
    while bob.getCenter().getX() <= 1000: 
        x += 3
        dy = (18 * pi * cos((3*pi*x)/1000) *sin((3*pi*x)/1000))/(5 * abs(sin((3*pi*x)/1000)))
        bob.move(3, dy)
        a += 0.5
        db = 0
        lily.move(a,db)
        c += 3
        dd = 4 * cos((c/900) + 18)/9
        joe.move(5, dd)

    while win.checkKey() != 'q':
        pass


#how to make grass and bunny simultanous
class Grass:
   def __init__(self, win, xp):
       self.xp = xp
       self.y = 0
       self.grass = Circle(Point(xp, self.y), 50)
       self.grass.setFill("lightgreen")
       self.grass.draw(win)

class Bunny:
   def __init__(self, win, x, y):
       x = randrange(0, 1000)
       y = 10 * abs(40 * sin((3 * pi/1000) * x))
       self.x = x
       self.y = y
       bob = Circle(Point(self.x, self.y), 50)
       bob.setFill("pink")
       bob.draw(win)
  
   def Bunmovement(self, win):
       while self.x <= 1000:
           self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
           bob = Circle(Point(self.x, self.y), 50)
           bob.setFill("pink")
           bob.draw(win)
           self.x = self.x + 33/2
           time.sleep(0.05)
           bob.undraw()
           if self.x > 1000:
               break
          
       while self.x > 0:
           self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
           bob = Circle(Point(self.x, self.y), 50)
           bob.setFill("pink")
           bob.draw(win)
           self.x = self.x - 33/2
           time.sleep(0.05)
           bob.undraw()
          


class Foxy:
   def __init__(self, win, x):
       x = randrange(0, 500)
       y = 100
       self.x = x
       self.y = y
       lily = Circle(Point(self.x, self.y), 50)
       lily.setFill("coral")
       lily.draw(win)

   def Foxmovement(self, win):
       while self.x <= 1000:
           self.y = 100
           lily = Circle(Point(self.x, self.y), 50)
           lily.setFill("coral")
           lily.draw(win)
           self.x = self.x + 33
           time.sleep(0.05)
           lily.undraw()
           if self.x > 1000:
               break
       while self.x > 0:
           self.y = 100
           lily = Circle(Point(self.x, self.y), 50)
           lily.setFill("coral")
           lily.draw(win)
           self.x = self.x - 33
           time.sleep(0.05)
           lily.undraw()

class Eagle:
   def __init__(self, win, x, y):
       x = randrange(0, 1000)
       y = 400 * sin((1/900)*self.x + 18) + 500
       self.x = x
       self.y = y
       joe = Circle(Point(self.x, self.y), 50)
       joe.setFill("peru")
       joe.draw(win)

  
   def Eagmovement(self, win):
       while self.x <= 1000:
           self.y = 400 * sin((1/900)*self.x + 18) + 500
           joe = Circle(Point(self.x, self.y), 50)
           joe.setFill("peru")
           joe.draw(win)
           self.x = self.x + 33/2
           time.sleep(0.05)
           joe.undraw()
           if self.x > 1000:
               break
          
       while self.x > 0:
           self.y = 400 * sin((1/900)*self.x + 18) + 500
           joe = Circle(Point(self.x, self.y), 50)
           joe.setFill("peru")
           joe.draw(win)
           self.x = self.x - 33/2
           time.sleep(0.05)
           joe.undraw()
main()

#Psuedo Code that doesn't work
'''
while run:
        if Bunny_instance.getCenter.getX() >= 1000:
            Bunny_instance.moveleft()
        else:
            Bunny_instance.moveright()
class Animal:
     rightedge = 1000
     leftedge = 0
     def duplicate(self):
       while True:
        if win.checkKey() == 'b':
            self.clone()
        if win.checkKey() == 'f':
            self.clone()
        if win.checkKey() == 'e':
            self.clone()
        if win.checkKey() == 'q':
            break
     def death(self):
       if self.getCenter.getX() <= other.getCenter.getX() + 20 and self.getCenter.getX() <= other.getCenter.getX() + 20
     def eat(self):
       pass


def moveright(self):
        self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
        self.x += 3
        dy = (18 * pi * cos((3*pi*self.x)/1000) *sin((3*pi*self.x)/1000))/(5 * abs(sin((3*pi*self.x)/1000)))

   def moveleft(self):
        self.y = 10 * abs(40 * sin((3*pi/1000) * self.x))
        self.x -= 3
        dy = (18 * pi * cos((3*pi*self.x)/1000) *sin((3*pi*self.x)/1000))/(5 * abs(sin((3*pi*self.x)/1000)))
  
'''

