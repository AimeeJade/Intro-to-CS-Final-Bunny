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
    message = Text(Point(800,880), '''Instructions:
Press "b" to add a bunny
Press "f" to add a fox
Press "e" to add an eagle
Press "g" to add more grass
Click on an object to delete it
Press "q" to exit the simulation''')
    message.setFace("courier")
    message.setTextColor("black")
    message.setSize(18)
    message.setStyle("normal")
    message.draw(win)


#--------------------------Creating Animal Instances at Random Points----------------------------
    #bunny 
    bun_x = randrange(0, 1000)
    bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
    bun = Bunny(bun_x, bun_y, True)
    bun.bun.draw(win)

    #fox
    fox_x = randrange(0, 1000)
    fox_y = 100
    fox = Fox(fox_x, fox_y, True)
    fox.fox.draw(win)
   
    #eagle
    eagle_x = randrange(0, 50)
    eagle_y = 400 * sin((1/90)* eagle_x + 18) + 350
    eagle = Eagle(eagle_x, eagle_y, True)
    eagle.eagle.draw(win)

#--------------------------Main While Loop for Interactions and Movements---------------------------
    clickPoint = win.checkKey()
    while clickPoint != 'q': 
        if clickPoint != "":
            print(clickPoint)
        bun_slope = (18 * pi * cos((3 * pi * bun_x) / 1000) * sin((3 * pi * bun_x) / 1000))/(5 * abs(sin((3 * pi * bun_x) / 1000)))
        fox_slope = 0
        eagle_slope = (150 * cos((eagle_x/90) + 18))/9
       
        
    #-------- eating interations ----------
        if bun.bun.getCenter().getX() >= grass_x - 5 and bun.bun.getCenter().getX() <= grass_x + 5:
            grass.grass.undraw()
            grass_x = choice(grass_choice)
            grass = Grass(grass_x)
            grass.grass.draw(win)

        if (fox.fox.getCenter().getY() >= bun.bun.getCenter().getY() - 60 and fox.fox.getCenter().getY() <= bun.bun.getCenter().getY() + 60) and (fox.fox.getCenter().getX() >= bun.bun.getCenter().getX() - 60 and fox.fox.getCenter().getX() <= bun.bun.getCenter().getX() + 60):
            bun.bun.undraw()
            #bun2.bun.draw(win)

        if (eagle.eagle.getCenter().getY() >= fox.fox.getCenter().getY() - 60 and eagle.eagle.getCenter().getY() <= fox.fox.getCenter().getY() + 60) and (eagle.eagle.getCenter().getX() >= fox.fox.getCenter().getX() - 60 and eagle.eagle.getCenter().getX() <= fox.fox.getCenter().getX() + 60):
            fox.fox.undraw()
        
        point = win.checkMouse()
        if point != None: 
            if (point.getY() >= bun.bun.getCenter().getY() - 60 and point.getY() <= bun.bun.getCenter().getY() + 60) and (point.getX() >= bun.bun.getCenter().getX() - 60 and point.getX() <= bun.bun.getCenter().getX() + 60):
                bun.bun.undraw()
            if (point.getY() >= fox.fox.getCenter().getY() - 60 and point.getY() <= fox.fox.getCenter().getY() + 60) and (point.getX() >= fox.fox.getCenter().getX() - 60 and point.getX() <= fox.fox.getCenter().getX() + 60):
                fox.fox.undraw()
            if (point.getY() >= eagle.eagle.getCenter().getY() - 60 and point.getY() <= eagle.eagle.getCenter().getY() + 60) and (point.getX() >= eagle.eagle.getCenter().getX() - 60 and point.getX() <= eagle.eagle.getCenter().getX() + 60):
                eagle.eagle.undraw()
            if (point.getY() >= grass.grass.getCenter().getY() - 60 and point.getY() <= grass.grass.getCenter().getY() + 60) and (point.getX() >= grass.grass.getCenter().getX() - 60 and point.getX() <= grass.grass.getCenter().getX() + 60):
                grass.grass.undraw()
        
# point stuff 
#why is the bunny not apearing? what is it not cloning???????
        if clickPoint == 'b':
            bun_x2 = randrange(0, 1000)
            bun_y2 = 10 * abs(40 * sin((3 * pi/1000) * bun_x2)) + 40
            bun2 = Bunny(bun_x2, bun_y2, True)
            bun2.bun.draw(win)
            bun2.bun_move(bun_slope)
            
    #---------------------------------------
        time.sleep(0.01)

    #Animal movements 
        bun.bun_move(bun_slope)
        fox.fox_move(fox_slope)
        eagle.eagle_move(eagle_slope)
        clickPoint = win.checkKey()
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
   def __init__(self, bun_x, bun_y, right):
       self.right = right
       self.x = bun_x
       self.y = bun_y
       self.bun = Circle(Point(self.x, self.y), 50)
       self.bun.setFill("pink")
   
   def bun_move(self, bun_slope):
       self.bun_slope = bun_slope
       if self.x > 1000: 
            self.x -= 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            self.bun.move(-3, -self.bun_slope)
            self.right = False

       elif self.x < 10:
            self.x += 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            self.bun.move(3, self.bun_slope)
            self.right = True
            

       if self.right: 
            self.x += 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            self.bun.move(3, self.bun_slope)

       else:
            self.x -= 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            self.bun.move(-3,-self.bun_slope)


class Fox:
   def __init__(self, fox_x, fox_y, right2):
       self.right2 = right2
       self.x = fox_x
       self.y = fox_y
       self.fox = Circle(Point(self.x, self.y), 50)
       self.fox.setFill("coral")

   def fox_move(self, fox_slope):
       self.fox_slope = fox_slope
       if self.x > 1000:
            self.x -= 10
            self.fox_slope = 0
            self.fox.move(-15, self.fox_slope)
            self.right2 = False
            
       elif self.x < 0:
            self.x += 10
            self.fox_slope = 0
            self.fox.move(15, self.fox_slope)
            self.right2 = True
            
       if self.right2:
            self.x += 10
            self.fox_slope = 0
            self.fox.move(15, self.fox_slope)
            
       else:
            self.x -= 10
            self.fox_slope = 0
            self.fox.move(-15, self.fox_slope)

class Eagle:
   def __init__(self, eagle_x, eagle_y, right3):
       self.right3 = right3
       self.x = eagle_x
       self.y = eagle_y
       self.eagle = Circle(Point(self.x, self.y), 50)
       self.eagle.setFill("peru")

   def eagle_move(self, eagle_slope):
       self.eagle_slope = eagle_slope
       if self.x > 1000:
            self.x -= 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(-5,-self.eagle_slope)
            self.right3 = False

       elif self.x < 0:
            self.x += 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(5,self.eagle_slope)
            self.right3 = True

       if self.right3:
            self.x += 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(5, self.eagle_slope)

       else:
            self.x -= 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(-5,-self.eagle_slope)


main()
