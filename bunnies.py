from graphics import *
from math import *
from random import *
import time
from tkinter import *
from PIL import Image
import numpy as np

im = Image.open('TBunny.png')
immat = im.load()
(X, Y) = im.size
m = np.zeros((X, Y))

for x in range(X):
    for y in range(Y):
        m[x, y] = immat[(x, y)] != (255, 255, 255)
m = m / np.sum(np.sum(m))

# marginal distributions
dx = np.sum(m, 1)
dy = np.sum(m, 0)

# expected values
cx = np.sum(dx * np.arange(X))
cy = np.sum(dy * np.arange(Y))

print(cx, cy)


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
    eagle_x = randrange(0, 1000)
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

        if (fox.fox.getCenter().getY() >= bun_y - 50 and fox.fox.getCenter().getY() <= bun_y + 50) and (fox.fox.getCenter().getX() >= bun_x - 50 and fox.fox.getCenter().getX() <= bun_x + 50):
            bun.bun.undraw()

        if (eagle.eagle.getCenter().getY() >= fox_y - 10 and eagle.eagle.getCenter().getY() <= fox_y + 10) and (eagle.eagle.getCenter().getX() >= fox_x - 10 and eagle.eagle.getCenter().getX() <= fox_x + 10):
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
        if fox_x > 1000:
            fox_x -= 10
            fox.fox.move(-10,0)
            right2 = False
        elif fox_x < 0:
            fox_x += 10
            fox.fox.move(10,0)
            right2 = True
        if right2:
            fox_x += 10
            fox.fox.move(10,0)
        else:
            fox_x -= 10
            fox.fox.move(-10,0)

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
