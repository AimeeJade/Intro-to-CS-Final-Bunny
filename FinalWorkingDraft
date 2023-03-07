from graphics import *
from math import *
from random import *
import time
#add description here of the main and figure out the courses folder thingy
def main():
    #creating a window and the background
    win = GraphWin("Bunny", 1000, 1000, autoflush = False)
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
    grass.grasstop.draw(win)
    #creating the textbook with instructions
    textbox = Textbox()
    textbox.box.draw(win)
    textbox.message.draw(win)
#--------------------------Creating Animal Instances at Random Points----------------------------
    #bunny instance
    bun_x = randrange(0, 1000)
    bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
    bun = Bunny(bun_x, bun_y, True)
    bun.bunear1.draw(win)
    bun.bunear2.draw(win)
    bun.buntail.draw(win)
    bun.bunbody.draw(win)
    bun.bun.draw(win)
    #fox instance
    fox_x = randrange(0, 1000)
    fox_y = 100
    fox = Fox(fox_x, fox_y, True)
    fox.fox.draw(win)
    fox.foxbody.draw(win)
    fox.foxear1.draw(win)
    fox.foxear2.draw(win)
    fox.foxtail.draw(win)
    fox.foxnose.draw(win)
   
    #eagle instance
    eagle_x = randrange(0, 50)
    eagle_y = 400 * sin((1/90)* eagle_x + 18) + 350
    eagle = Eagle(eagle_x, eagle_y, True)
    eagle.eaglebody.draw(win)
    eagle.eaglewing1.draw(win)
    eagle.eaglewing2.draw(win)
    eagle.eagle.draw(win)
    eagle.eaglebeak.draw(win)
    
#--------------------------Main While Loop for Interactions and Movements---------------------------
    #---------creating object lists----------
    #bunny shapes lists
    bunny_list = [bun]
    bunny_body_list = [bun.bunbody]
    bunny_ear1_list = [bun.bunear1]
    bunny_ear2_list = [bun.bunear2]
    bunny_tail_list = [bun.buntail]
    #bunny shapes lists
    fox_list = [fox]
    fox_body_list = [fox.foxbody]
    fox_ear1_list = [fox.foxear1]
    fox_ear2_list = [fox.foxear2]
    fox_tail_list = [fox.foxtail]
    fox_nose_list = [fox.foxnose]
    #bunny shapes lists
    eagle_list = [eagle]
    eagle_body_list = [eagle.eaglebody]
    eagle_wing1_list = [eagle.eaglewing1]
    eagle_wing2_list = [eagle.eaglewing2]
    eagle_beak_list = [eagle.eaglebeak]
    #bunny shapes list
    grass_list = [grass]
    grass_top_list = [grass.grasstop]
    clickPoint = win.checkKey()
    while clickPoint != 'q': 
        if clickPoint != "":
            print(clickPoint)
        #object slopes for movement
        bun_slope = (18 * pi * cos((3 * pi * bun_x) / 1000) * sin((3 * pi * bun_x) / 1000))/(5 * abs(sin((3 * pi * bun_x) / 1000)))
        fox_slope = 0
        eagle_slope = (150 * cos((eagle_x/90) + 18))/9
       
        
    #--------------------- eating interations ------------------------
        # for each bunny in the bunny list, if the center of the bunny is in the range of the center of the grass, the bunny eats the grass
        for i in bunny_list:
            if i.bun.getCenter().getX() >= grass_x - 5 and i.bun.getCenter().getX() <= grass_x + 5:
                
                grass.grass.undraw()
                grass.grasstop.undraw()
                grass_x = choice(grass_choice)
                grass = Grass(grass_x)
                
                #grass ia drawn again, elsewhere (and it could also appear in the same spot)
                grass.grass.draw(win)
                grass.grasstop.draw(win) 
            #when fox is in range of a bunny, it eats the bunny
            for f in fox_list:
                if (f.fox.getCenter().getY() >= i.bun.getCenter().getY() - 60 and f.fox.getCenter().getY() <= i.bun.getCenter().getY() + 60) and (f.fox.getCenter().getX() >= i.bun.getCenter().getX() - 60 and f.fox.getCenter().getX() <= i.bun.getCenter().getX() + 60):
                    i.bun.undraw()
                    i.bunbody.undraw()
                    i.bunear1.undraw()
                    i.bunear2.undraw()
                    i.buntail.undraw()
                    count = bunny_list.index(i)
                    print(count)
                    del bunny_list[count]
                    del bunny_body_list[count]
                    del bunny_ear1_list[count]
                    del bunny_ear2_list[count]
                    del bunny_tail_list[count]
                    
        for i in fox_list:
            if (eagle.eagle.getCenter().getY() >= i.fox.getCenter().getY() - 60 and eagle.eagle.getCenter().getY() <= i.fox.getCenter().getY() + 60) and (eagle.eagle.getCenter().getX() >= i.fox.getCenter().getX() - 60 and eagle.eagle.getCenter().getX() <= i.fox.getCenter().getX() + 60):
                i.fox.undraw()
                i.foxbody.undraw()
                i.foxear1.undraw()
                i.foxear2.undraw()
                i.foxtail.undraw()
                i.foxnose.undraw()
                count = fox_list.index(i)
                print(count)
                del fox_list[count]
                del fox_body_list[count]
                del fox_ear1_list[count]
                del fox_ear2_list[count]
                del fox_tail_list[count]
                del fox_nose_list[count]
        
    #--------when the mouse click falls into a certain range around the center of the animal object, the object is undrawn--------
        point = win.checkMouse()
        if point != None: 
            for i in bunny_list:
                if (point.getY() >= i.bun.getCenter().getY() - 60 and point.getY() <= i.bun.getCenter().getY() + 60) and (point.getX() >= i.bun.getCenter().getX() - 60 and point.getX() <= i.bun.getCenter().getX() + 60):
                    i.bun.undraw()
                    i.bunbody.undraw()
                    i.bunear1.undraw()
                    i.bunear2.undraw()
                    i.buntail.undraw()
                    count2 = bunny_list.index(i)
                    del bunny_list[count2]
                    del bunny_body_list[count2]
                    del bunny_ear1_list[count2]
                    del bunny_ear2_list[count2]
                    del bunny_tail_list[count2]
            for i in fox_list:
                if (point.getY() >= i.fox.getCenter().getY() - 60 and point.getY() <= i.fox.getCenter().getY() + 60) and (point.getX() >= i.fox.getCenter().getX() - 60 and point.getX() <= i.fox.getCenter().getX() + 60):
                    i.fox.undraw()
                    i.foxbody.undraw()
                    i.foxear1.undraw()
                    i.foxear2.undraw()
                    i.foxtail.undraw()
                    i.foxnose.undraw()
                    count2 = fox_list.index(i)
                    del fox_list[count2]
                    del fox_body_list[count2]
                    del fox_ear1_list[count2]
                    del fox_ear2_list[count2]
                    del fox_tail_list[count2]
                    del fox_nose_list[count2]
            for i in eagle_list:
                if (point.getY() >= i.eagle.getCenter().getY() - 60 and point.getY() <= i.eagle.getCenter().getY() + 60) and (point.getX() >= i.eagle.getCenter().getX() - 60 and point.getX() <= i.eagle.getCenter().getX() + 60):
                    i.eagle.undraw()
                    i.eaglebody.undraw()
                    i.eaglewing1.undraw()
                    i.eaglewing2.undraw()
                    i.eaglebeak.undraw()
                    count2 = eagle_list.index(i)
                    del eagle_list[count2]
                    del eagle_body_list[count2]
                    del eagle_wing1_list[count2]
                    del eagle_wing2_list[count2]
                    del eagle_beak_list[count2]
            for i in grass_list:
                if (point.getY() >= i.grass.getCenter().getY() - 60 and point.getY() <= i.grass.getCenter().getY() + 60) and (point.getX() >= i.grass.getCenter().getX() - 60 and point.getX() <= i.grass.getCenter().getX() + 60):
                    i.grass.undraw()
                    i.grasstop.undraw()
                    del grass_list[0]
                    del grass_top_list[0]
        #how to make the bunny move?
        if clickPoint == 'b':
            bun_x = randrange(0, 1000)
            bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
            bun = Bunny(bun_x, bun_y, True)
            bun.bunbody.draw(win)
            bun.bunear1.draw(win)
            bun.bunear2.draw(win)
            bun.buntail.draw(win)
            bun.bun.draw(win)
            bunny_list.append(bun)
            bunny_body_list.append(bun.bunbody)
            bunny_ear1_list.append(bun.bunear1)
            bunny_ear2_list.append(bun.bunear2)
            bunny_tail_list.append(bun.buntail)
        if clickPoint == 'f':
            fox_x = randrange(0, 1000)
            fox_y = 100
            fox = Fox(fox_x, fox_y, True)
            fox.fox.draw(win)
            fox.foxbody.draw(win)
            fox.foxear1.draw(win)
            fox.foxear2.draw(win)
            fox.foxtail.draw(win)
            fox.foxnose.draw(win)
            fox_list.append(fox)
            fox_body_list.append(fox.foxbody)
            fox_ear1_list.append(fox.foxear1)
            fox_ear2_list.append(fox.foxear2)
            fox_tail_list.append(fox.foxtail)
            fox_nose_list.append(fox.foxnose)
        if clickPoint == 'e':
            eagle_x = randrange(0, 100)
            eagle_y = 10 * abs(40 * sin((3 * pi/1000) * eagle_x)) + 40
            eagle = Eagle(eagle_x, eagle_y, True)
            eagle.eaglebody.draw(win)
            eagle.eaglewing1.draw(win)
            eagle.eaglewing2.draw(win)
            eagle.eagle.draw(win)
            eagle.eaglebeak.draw(win)
            eagle_list.append(eagle)
            eagle_body_list.append(eagle.eaglebody)
            eagle_wing1_list.append(eagle.eaglewing1)
            eagle_wing2_list.append(eagle.eaglewing2)
            eagle_beak_list.append(eagle.eaglebeak)
        if clickPoint == 'g':
            grass_choice = [0, 1000/3, 2000/3, 1000]
            grass_x = choice(grass_choice)
            grass = Grass(grass_x)
            grass.grass.draw(win)
            grass.grasstop.draw(win)
            grass_list.append(grass)
            grass_top_list.append(grass.grasstop)
        update(30)
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
Click on an animal head to delete
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
       self.grasstop = Polygon(Point(self.grass_x, 90), Point(self.grass_x + 60, 0), Point(self.grass_x - 60, 0))
       self.grasstop.setFill("forest green")
    
class Bunny:
   def __init__(self, bun_x, bun_y, right):
       self.right = right
       self.x = bun_x
       self.y = bun_y
       self.bunear1 = Oval(Point(self.x - 5, self.y + 140), Point(self.x -45, self.y + 40))
       self.bunear1.setFill("pink")
       self.bunear2 = Oval(Point(self.x + 45, self.y + 140), Point(self.x + 5, self.y + 40))
       self.bunear2.setFill("pink")
       self.bunbody = Circle(Point(self.x, self.y - 90), 60)
       self.bunbody.setFill("pink")
       self.bun = Circle(Point(self.x, self.y), 50)
       self.bun.setFill("pink")
       self.buntail = Circle(Point(self.x + 60, self.y - 90), 20)
       self.buntail.setFill("white")
   
   def bun_move(self, bun_slope):
       self.bun_slope = bun_slope
       if self.x > 1000: 
            self.x -= 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            self.bunear1.move(-3, -self.bun_slope)
            self.bunear2.move(-3, -self.bun_slope)
            self.bunbody.move(-3, -self.bun_slope)
            self.bun.move(-3, -self.bun_slope)
            self.buntail.move(-3, -self.bun_slope)
            self.right = False
       elif self.x < 10:
            self.x += 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            
            self.bunear1.move(3, self.bun_slope)
            self.bunear2.move(3, self.bun_slope)
            self.bunbody.move(3, self.bun_slope)
            self.bun.move(3, self.bun_slope)
            self.buntail.move(3, self.bun_slope)
            self.right = True
            
       if self.right: 
            self.x += 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            self.bunear1.move(3, self.bun_slope)
            self.bunear2.move(3, self.bun_slope)
            self.bunbody.move(3, self.bun_slope)
            self.bun.move(3, self.bun_slope)
            self.buntail.move(3, self.bun_slope)
       else:
            self.x -= 3
            self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
            self.bunear1.move(-3, -self.bun_slope)
            self.bunear2.move(-3, -self.bun_slope)
            self.bunbody.move(-3, -self.bun_slope)
            self.bun.move(-3, -self.bun_slope)
            self.buntail.move(-3, -self.bun_slope)
class Fox:
   def __init__(self, fox_x, fox_y, right2):
       self.right2 = right2
       self.x = fox_x
       self.y = fox_y
       self.fox = Circle(Point(self.x, self.y), 50)
       self.fox.setFill("coral")
       self.foxbody = Circle(Point(self.x, self.y-90), 50)
       self.foxbody.setFill("coral")
       self.foxear1 = Polygon(Point(self.x-50, self.y +20), Point(self.x-90, self.y+70), Point(self.x -20, self.y+50))
       self.foxear1.setFill("coral")
       self.foxear2 = Polygon(Point(self.x+50, self.y +20), Point(self.x+90, self.y+70), Point(self.x +20, self.y+50))
       self.foxear2.setFill("coral")
       self.foxtail = Polygon(Point(self.x + 50, self.y - 90), Point(self.x + 150, self.y -30), Point(self.x + 90, self.y - 100))
       self.foxtail.setFill("coral")
       self.foxnose = Polygon(Point(self.x, self.y - 10), Point(self.x + 10, self.y), Point(self.x - 10, self.y))
       self.foxnose.setFill("black")
   def fox_move(self, fox_slope):
       self.fox_slope = fox_slope
       if self.x > 1000:
            self.x -= 10
            self.fox_slope = 0
            self.fox.move(-15, self.fox_slope)
            self.foxbody.move(-15, self.fox_slope)
            self.foxear1.move(-15, self.fox_slope)
            self.foxear2.move(-15, self.fox_slope)
            self.foxtail.move(-15, self.fox_slope)
            self.foxnose.move(-15, self.fox_slope)
            self.right2 = False
            
       elif self.x < 0:
            self.x += 10
            self.fox_slope = 0
            self.fox.move(15, self.fox_slope)
            self.foxbody.move(15, self.fox_slope)
            self.foxear1.move(15, self.fox_slope)
            self.foxear2.move(15, self.fox_slope)
            self.foxtail.move(15, self.fox_slope)
            self.foxnose.move(15, self.fox_slope)
            self.right2 = True
            
       if self.right2:
            self.x += 10
            self.fox_slope = 0
            self.fox.move(15, self.fox_slope)
            self.foxbody.move(15, self.fox_slope)
            self.foxear1.move(15, self.fox_slope)
            self.foxear2.move(15, self.fox_slope)
            self.foxtail.move(15, self.fox_slope)
            self.foxnose.move(15, self.fox_slope)
            
       else:
            self.x -= 10
            self.fox_slope = 0
            self.fox.move(-15, self.fox_slope)
            self.foxbody.move(-15, self.fox_slope)
            self.foxear1.move(-15, self.fox_slope)
            self.foxear2.move(-15, self.fox_slope)
            self.foxtail.move(-15, self.fox_slope)
            self.foxnose.move(-15, self.fox_slope)
class Eagle:
   def __init__(self, eagle_x, eagle_y, right3):
       self.right3 = right3
       self.x = eagle_x
       self.y = eagle_y
       self.eagle = Circle(Point(self.x, self.y), 50)
       self.eagle.setFill("white")
       self.eaglebody = Circle(Point(self.x, self.y-90), 50)
       self.eaglewing1 = Polygon(Point(self.x +10, self.y - 40), Point(self.x + 150, self.y+30), Point(self.x +110, self.y -40))
       self.eaglewing2 = Polygon(Point(self.x -10, self.y - 40), Point(self.x - 150, self.y+30), Point(self.x -110, self.y -40))
       self.eaglebeak = Polygon(Point(self.x-20, self.y), Point(self.x+20, self.y), Point(self.x, self.y-25))
       self.eaglebeak.setFill("yellow")
       self.eaglebody.setFill("peru")
       self.eaglewing1.setFill("peru")
       self.eaglewing2.setFill("peru")
   def eagle_move(self, eagle_slope):
       self.eagle_slope = eagle_slope
       if self.x > 1000:
            self.x -= 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(-5,-self.eagle_slope)
            self.eaglebody.move(-5,-self.eagle_slope)
            self.eaglewing1.move(-5,-self.eagle_slope)
            self.eaglewing2.move(-5,-self.eagle_slope)
            self.eaglebeak.move(-5,-self.eagle_slope)
            self.right3 = False
       elif self.x < 0:
            self.x += 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(5,self.eagle_slope)
            self.eaglebody.move(5,self.eagle_slope)
            self.eaglewing1.move(5,self.eagle_slope)
            self.eaglewing2.move(5,self.eagle_slope)
            self.eaglebeak.move(5,self.eagle_slope)
            self.right3 = True
       if self.right3:
            self.x += 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(5, self.eagle_slope)
            self.eaglebody.move(5,self.eagle_slope)
            self.eaglewing1.move(5,self.eagle_slope)
            self.eaglewing2.move(5,self.eagle_slope)
            self.eaglebeak.move(5,self.eagle_slope)
       else:
            self.x -= 5
            self.eagle_slope = (150 * cos((self.x/90) + 18))/9
            self.eagle.move(-5,-self.eagle_slope)
            self.eaglebody.move(-5,-self.eagle_slope)
            self.eaglewing1.move(-5,-self.eagle_slope)
            self.eaglewing2.move(-5,-self.eagle_slope)
            self.eaglebeak.move(-5,-self.eagle_slope)
main()
