from graphics import *
from math import *
from random import *
import time


def main():

    #creating a window and the background
    win = GraphWin("Bunny", 1000, 1000)
    win.setBackground("light cyan")
    win.setCoords(0, 0, 1000, 1000)
    ground = Ground()
    ground.ground.draw(win)
    grass_choice = [0, 1000/3, 2000/3, 1000]
    grass_x = choice(grass_choice)
    grass = Grass(grass_x)
    grass.grass.draw(win)

#------------------------------------------------------
    #bunny 
    bun_x = randrange(0, 1000)
    bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
    bun = Bunny(bun_x, bun_y)
    bun.bun.draw(win)
    
    #fox
    fox_x = randrange(0, 1000)
    fox_y = 100
    fox = Foxy(fox_x, fox_y)
    fox.fox.draw(win)
   
    #eagle
    eagle_x = randrange(0, 100)
    eagle_y = 400 * sin((1/90)* eagle_x + 18) + 350
    eagle = Eagle(eagle_x, eagle_y)
    eagle.eagle.draw(win)
#------------------------------------------------------

    right = True
    right2 = True
    right3 = True
    
    while win.checkKey() != 'q': 
        bun_slope = (18 * pi * cos((3 * pi * bun_x) / 1000) * sin((3 * pi * bun_x) / 1000))/(5 * abs(sin((3 * pi * bun_x) / 1000)))
        eagle_slope = (140 * cos((eagle_x/90) + 18))/9
        
        #eating interation
        if bun.bun.getCenter().getX() >= grass_x - 5 and bun.bun.getCenter().getX() <= grass_x + 5:
            grass.grass.undraw()
            grass_x = choice(grass_choice)
            grass = Grass(grass_x)
            grass.grass.draw(win)

        if (fox.fox.getCenter().getY() >= bun.bun.getCenter().getY() - 60 and fox.fox.getCenter().getY() <= bun.bun.getCenter().getY() + 60) and (fox.fox.getCenter().getX() >= bun.bun.getCenter().getX() - 60 and fox.fox.getCenter().getX() <= bun.bun.getCenter().getX() + 60):
            bun.bun.undraw()

        if (eagle.eagle.getCenter().getY() >= fox.fox.getCenter().getY() - 60 and eagle.eagle.getCenter().getY() <= fox.fox.getCenter().getY() + 60) and (eagle.eagle.getCenter().getX() >= fox.fox.getCenter().getX() - 60 and eagle.eagle.getCenter().getX() <= fox.fox.getCenter().getX() + 60):
            fox.fox.undraw()

    
        time.sleep(0.01)

        #bunny movement
        if bun_x > 1000: 
            bun_x -= 3
            bun.bun.move(-3, -bun_slope)
            right = False
        elif bun_x < 0:
            bun_x += 3
            bun.bun.move(3, bun_slope)
            right = True
        if right: #movement based on the direction given by "right" variable
            bun_x += 3
            bun.bun.move(3, bun_slope)
        else:
            bun_x -= 3
            bun.bun.move(-3,-bun_slope)
            
        #fox movement
        if fox_x > 980:
            fox_x -= 10
            fox.fox.move(-15,0)
            right2 = False
        elif fox_x < 20:
            fox_x += 10
            fox.fox.move(15,0)
            right2 = True
        if right2:
            fox_x += 10
            fox.fox.move(15,0)
        else:
            fox_x -= 10
            fox.fox.move(-15,0)

        #eagle movement
        if eagle_x > 1000:
            eagle_x -= 5
            eagle.eagle.move(-5,-eagle_slope)
            right3 = False
        elif eagle_x < 0:
            eagle_x += 5
            eagle.eagle.move(5,eagle_slope)
            right3 = True
        if right3:
            eagle_x += 5
            eagle.eagle.move(5,eagle_slope)
        else:
            eagle_x -= 5
            eagle.eagle.move(-5,-eagle_slope)
    
#classes
class Ground:
    def __init__(self):
        self.ground = Line(Point(0, 30), Point(1000, 30))
        self.ground.setOutline("lightgreen")
        self.ground.setWidth(60)

class Grass:
   def __init__(self, grass_x):
       self.grass_x = grass_x
       self.y = 0
       self.grass = Circle(Point(grass_x, self.y), 50)
       self.grass.setFill("lightgreen")
    
class Bunny:
   def __init__(self, bun_x, bun_y):
       #x = randrange(0, 1000)
       #y = 10 * abs(40 * sin((3 * pi/1000) * x))
       self.x = bun_x
       self.y = bun_y
       self.bun = Circle(Point(self.x, self.y), 50)
       self.bun.setFill("pink")
   
   def bun_move_right(self, dy):
       self.x -= 3
       self.dy = dy
       self.bun.move(-3, -self.dy)


class Foxy:
   def __init__(self, fox_x, fox_y):
       #x = randrange(0, 500)
       #y = 100
       self.x = fox_x
       self.y = fox_y
       self.fox = Circle(Point(self.x, self.y), 50)
       self.fox.setFill("coral")


class Eagle:
   def __init__(self, eagle_x, eagle_y):
       #x = randrange(0, 1000)
       #y = 400 * sin((1/900)*self.x + 18) + 500
       self.x = eagle_x
       self.y = eagle_y
       self.eagle = Circle(Point(self.x, self.y), 50)
       self.eagle.setFill("peru")


main()

''' WRONG FOR THE MOVEMENT WHEN I TRY TO MAKE IT A METHOD. IDK WHY
from graphics import *
from math import *
from random import *
import time


def main():

    #creating a window and the background
    win = GraphWin("Bunny", 1000, 1000)
    win.setBackground("light cyan")
    win.setCoords(0, 0, 1000, 1000)
    ground = Ground()
    ground.ground.draw(win)
    grass_choice = [0, 1000/3, 2000/3, 1000]
    grass_x = choice(grass_choice)
    grass = Grass(grass_x)
    grass.grass.draw(win)

#--------------------------Creating Animal Instances at Random Points----------------------------
    #bunny 
    bun_x = randrange(0, 1000)
    bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
    bun = Bunny(bun_x, bun_y)
    bun.bun.draw(win)
    
    #fox
    fox_x = randrange(0, 1000)
    fox_y = 100
    fox = Foxy(fox_x, fox_y)
    fox.fox.draw(win)
   
    #eagle
    eagle_x = randrange(0, 100)
    eagle_y = 400 * sin((1/90)* eagle_x + 18) + 350
    eagle = Eagle(eagle_x, eagle_y)
    eagle.eagle.draw(win)

#--------------------------Main While Loop for Interactions and Movements---------------------------
    right = True
    right2 = True
    right3 = True
    
    while win.checkKey() != 'q': 
        bun_slope = (18 * pi * cos((3 * pi * bun_x) / 1000) * sin((3 * pi * bun_x) / 1000))/(5 * abs(sin((3 * pi * bun_x) / 1000)))
        eagle_slope = (140 * cos((eagle_x/90) + 18))/9
        
        #eating interation
        if bun.bun.getCenter().getX() >= grass_x - 5 and bun.bun.getCenter().getX() <= grass_x + 5:
            grass.grass.undraw()
            grass_x = choice(grass_choice)
            grass = Grass(grass_x)
            grass.grass.draw(win)

        if (fox.fox.getCenter().getY() >= bun.bun.getCenter().getY() - 60 and fox.fox.getCenter().getY() <= bun.bun.getCenter().getY() + 60) and (fox.fox.getCenter().getX() >= bun.bun.getCenter().getX() - 60 and fox.fox.getCenter().getX() <= bun.bun.getCenter().getX() + 60):
            bun.bun.undraw()

        if (eagle.eagle.getCenter().getY() >= fox.fox.getCenter().getY() - 60 and eagle.eagle.getCenter().getY() <= fox.fox.getCenter().getY() + 60) and (eagle.eagle.getCenter().getX() >= fox.fox.getCenter().getX() - 60 and eagle.eagle.getCenter().getX() <= fox.fox.getCenter().getX() + 60):
            fox.fox.undraw()

        time.sleep(0.01)

        #bunny movement
        bun.bun_move(bun_slope, right)
            
        #fox movement
        fox.fox_move(right2)

        #eagle movement
        eagle.eagle_move(eagle_slope, right3)
    
#--------------------------------------------- classes ------------------------------------------------
class Ground:
    def __init__(self):
        self.ground = Line(Point(0, 30), Point(1000, 30))
        self.ground.setOutline("lightgreen")
        self.ground.setWidth(60)

class Grass:
   def __init__(self, grass_x):
       self.grass_x = grass_x
       self.y = 0
       self.grass = Circle(Point(grass_x, self.y), 50)
       self.grass.setFill("lightgreen")
    
class Bunny:
   def __init__(self, bun_x, bun_y):
       self.x = bun_x
       self.y = bun_y
       self.bun = Circle(Point(self.x, self.y), 50)
       self.bun.setFill("pink")
   
   def bun_move(self, bun_slope, right):
       self.right = right
       self.bun_slope = bun_slope
       if self.x > 1000: 
            self.x -= 3
            self.bun.move(-3, -self.bun_slope)
            self.right = False
       elif self.x < 0:
            self.x += 3
            self.bun.move(3, self.bun_slope)
            self.right = True
       if right: #movement based on the direction given by "right" variable
            self.x += 3
            self.bun.move(3, self.bun_slope)
       else:
            self.x -= 3
            self.bun.move(-3,-self.bun_slope)


class Foxy:
   def __init__(self, fox_x, fox_y):
       #x = randrange(0, 500)
       #y = 100
       self.x = fox_x
       self.y = fox_y
       self.fox = Circle(Point(self.x, self.y), 50)
       self.fox.setFill("coral")

   def fox_move(self, right2):
       self.right2 = right2
       if self.x > 980:
            self.x -= 10
            self.fox.move(-15,0)
            right2 = False
       elif self.x < 20:
            self.x += 10
            self.fox.move(15,0)
            right2 = True
       if right2:
            self.x += 10
            self.fox.move(15,0)
       else:
            self.x -= 10
            self.fox.move(-15,0)

class Eagle:
   def __init__(self, eagle_x, eagle_y):
       self.x = eagle_x
       self.y = eagle_y
       self.eagle = Circle(Point(self.x, self.y), 50)
       self.eagle.setFill("peru")

   def eagle_move(self, eagle_slope, right3):
       self.right3 = right3
       if self.x > 1000:
            self.x -= 5
            self.eagle.move(-5,-eagle_slope)
            right3 = False
       elif self.x < 0:
            self.x += 5
            self.eagle.move(5,eagle_slope)
            right3 = True
       if right3:
            self.x += 5
            self.eagle.move(5,eagle_slope)
       else:
            self.x -= 5
            self.eagle.move(-5,-eagle_slope)


main()
'''
