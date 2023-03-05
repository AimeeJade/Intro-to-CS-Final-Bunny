from graphics import *
from math import *
from random import *
import time


def main():

    #creating a window and the background
    win = GraphWin("Bunny", 1000, 1000)
    win.setBackground("light cyan")
    win.setCoords(0, 0, 1000, 1000)
    
    #creating a green ground
    ground = Ground()
    ground.ground.draw(win)

    #creating the grass object
    grass_choice = [0, 1000/3, 2000/3, 1000]
    grass_x = choice(grass_choice)
    grass = Grass(grass_x)
    grass.grass.draw(win)

    #creating the textbook with instructions
    textbox = Textbox()
    textbox.box.draw(win)
    textbox.message.draw(win)


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
    bunny_list = [bun]
    fox_list = [fox]
    eagle_list = [eagle]

    clickPoint = win.checkKey()
    
    while clickPoint != 'q': 
        if clickPoint != "":
            print(clickPoint)
        bun_slope = (18 * pi * cos((3 * pi * bun_x) / 1000) * sin((3 * pi * bun_x) / 1000))/(5 * abs(sin((3 * pi * bun_x) / 1000)))
        fox_slope = 0
        eagle_slope = (150 * cos((eagle_x/90) + 18))/9
       
        
    #--------------------- eating interations ------------------------
        for i in bunny_list:
            if i.bun.getCenter().getX() >= grass_x - 5 and i.bun.getCenter().getX() <= grass_x + 5:
                grass.grass.undraw()
                grass_x = choice(grass_choice)
                grass = Grass(grass_x)
                grass.grass.draw(win)

            if (fox.fox.getCenter().getY() >= i.bun.getCenter().getY() - 60 and fox.fox.getCenter().getY() <= i.bun.getCenter().getY() + 60) and (fox.fox.getCenter().getX() >= i.bun.getCenter().getX() - 60 and fox.fox.getCenter().getX() <= i.bun.getCenter().getX() + 60):
                i.bun.undraw()

        for i in fox_list:
            if (eagle.eagle.getCenter().getY() >= i.fox.getCenter().getY() - 60 and eagle.eagle.getCenter().getY() <= i.fox.getCenter().getY() + 60) and (eagle.eagle.getCenter().getX() >= i.fox.getCenter().getX() - 60 and eagle.eagle.getCenter().getX() <= i.fox.getCenter().getX() + 60):
                i.fox.undraw()
        
    #--------when the mouse click falls into a certain range around the center of the animal object, the object is undrawn--------
        point = win.checkMouse()

        if point != None: 
            for i in bunny_list:
                if (point.getY() >= i.bun.getCenter().getY() - 60 and point.getY() <= i.bun.getCenter().getY() + 60) and (point.getX() >= i.bun.getCenter().getX() - 60 and point.getX() <= i.bun.getCenter().getX() + 60):
                    i.bun.undraw()

            for i in fox_list:
                if (point.getY() >= i.fox.getCenter().getY() - 60 and point.getY() <= i.fox.getCenter().getY() + 60) and (point.getX() >= i.fox.getCenter().getX() - 60 and point.getX() <= i.fox.getCenter().getX() + 60):
                    i.fox.undraw()

            for i in eagle_list:
                if (point.getY() >= i.eagle.getCenter().getY() - 60 and point.getY() <= i.eagle.getCenter().getY() + 60) and (point.getX() >= i.eagle.getCenter().getX() - 60 and point.getX() <= i.eagle.getCenter().getX() + 60):
                    i.eagle.undraw()

            if (point.getY() >= grass.grass.getCenter().getY() - 60 and point.getY() <= grass.grass.getCenter().getY() + 60) and (point.getX() >= grass.grass.getCenter().getX() - 60 and point.getX() <= grass.grass.getCenter().getX() + 60):
                grass.grass.undraw()

        #how to make the bunny move?
        if clickPoint == 'b':
            bun_x = randrange(0, 1000)
            bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
            bun = Bunny(bun_x, bun_y, True)
            bun.bun.draw(win)
            bunny_list.append(bun)

        if clickPoint == 'f':
            fox_x = randrange(0, 1000)
            fox_y = 100
            fox = Fox(fox_x, fox_y, True)
            fox.fox.draw(win)
            fox_list.append(fox)

        if clickPoint == 'e':
            eagle_x = randrange(0, 100)
            eagle_y = 10 * abs(40 * sin((3 * pi/1000) * eagle_x)) + 40
            eagle = Eagle(eagle_x, eagle_y, True)
            eagle.eagle.draw(win)
            eagle_list.append(eagle)

        time.sleep(0.01)

    #-------- Animal movements --------
        for i in bunny_list:
            i.bun_move(bun_slope)

        for i in fox_list:
            i.fox_move(fox_slope)

        for i in eagle_list:
            i.eagle_move(eagle_slope)

        clickPoint = win.checkKey()
#--------------------------------------------- classes ------------------------------------------------
class Ground:
    def __init__(self):
        self.ground = Line(Point(0, 30), Point(1000, 30))
        self.ground.setOutline("lightgreen")
        self.ground.setWidth(60)

class Textbox:
    def __init__(self):
       self.box = Rectangle(Point(670, 770), Point(930, 970))
       self.message = Text(Point(800,880), '''Instructions:
Press "b" to add a bunny
Press "f" to add a fox
Press "e" to add an eagle
Press "g" to add more grass
Click on an object to delete it
Press "q" to exit the simulation''')
       self.message.setFace("times roman")
       self.message.setTextColor("dark slate blue")
       self.message.setSize(18)
       self.message.setStyle("normal")

class Grass:
   def __init__(self, grass_x):
       self.grass_x = grass_x
       self.y = 0
       self.grass = Circle(Point(grass_x, self.y), 50)
       self.grass.setFill("forest green")
    
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
