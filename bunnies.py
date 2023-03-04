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
    y = 10 * abs(40 * sin((3 * pi/1000) * x)) + 40
    bun = Bunny(x, y)
    bun.bun.draw(win)
    #fox
    a = randrange(0, 1000)
    b = 100
    fox = Foxy(a, b)
    fox.fox.draw(win)
    #eagle
    c = randrange(0, 1000)
    d = 400 * sin((1/90)* c + 18) + 350
    eagle = Eagle(c, d)
    eagle.eagle.draw(win)

    right = True
    right2 = True
    right3 = True
    #main while loop
    while win.checkKey() != 'q': 
        dy = (18 * pi * cos((3*pi*x)/1000) *sin((3*pi*x)/1000))/(5 * abs(sin((3*pi*x)/1000)))
        dd = (140 * cos((c/90) + 18))/9
        
        if bun.bun.getCenter().getX() >= xp - 5 and bun.bun.getCenter().getX() <= xp + 5:
            grass.grass.undraw()
            xp = choice(xposition)
            grass = Grass(xp)
            grass.grass.draw(win)
        if fox.fox.getCenter().getY() >= y - 10 and fox.fox.getCenter().getY() <= y + 10:
            bun.bun.undraw()
        if eagle.eagle.getCenter().getY() >= b - 10 and eagle.eagle.getCenter().getY() <= b + 10:
            fox.fox.undraw()

    #circle 1 movement
        time.sleep(0.01)

        
        if x > 1000: #checking to change direction if the circle is out of bounds on either end
            x -= 3
            bun.bun.move(-3, -dy)
            right = False
        elif x < 0:
            x += 3
            bun.bun.move(3, dy)
            right = True
        if right: #movement based on the direction given by "right" variable
            x += 3
            bun.bun.move(3, dy)
        else:
            x -= 3
            bun.bun.move(-3,-dy)
            
    #fox movement
    
        if a > 1000:
            a -= 10
            fox.fox.move(-10,0)
            right2 = False
        elif a < 0:
            a += 10
            fox.fox.move(10,0)
            right2 = True
        if right2:
            a += 10
            fox.fox.move(10,0)
        else:
            a -= 10
            fox.fox.move(-10,0)

        #eagle
        if c > 1000:
            c -= 5
            eagle.eagle.move(-5,-dd)
            right3 = False
        elif c < 0:
            c += 5
            eagle.eagle.move(5,dd)
            right3 = True
        if right3:
            c += 5
            eagle.eagle.move(5,dd)
        else:
            c -= 5
            eagle.eagle.move(-5,-dd)
    

class Ground:
    def __init__(self):
        self.ground = Line(Point(0, 30), Point(1000, 30))
        self.ground.setOutline("lightgreen")
        self.ground.setWidth(60)
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
