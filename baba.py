from graphics import *
from math import *
from random import *

# -----------------------------------------------------------------------------------------------------------------------------------------
# DESCRIPTION:
# For the  main function, each of the classes are called and drawn to the window. In the main while loop (when 'q' is not pressed),
# animals interact (depending on position in food chain) and eat each other when they are within a specified range of each other's heads.
# Animals and grass can be duplicated by pressing a specific key, and can also be deleted when their 'head' is clicked.
# -----------------------------------------------------------------------------------------------------------------------------------------


def main():
    # creating a window and the background (can change window size to fit screen -- if 1000, 1000 is too big, we recommend 800, 800)
    win = GraphWin("Bunny", 1000, 1000, autoflush=False)
    win.setBackground("light cyan")
    win.setCoords(0, 0, 1000, 1000)

    # creating a green ground
    ground = Ground()
    ground.ground.draw(win)

    # creating the grass object
    grass_choice = [0, 1000/3, 2000/3, 1000]
    grass_x = choice(grass_choice)
    grass = Grass(grass_x)
    grass.grass.draw(win)
    grass.grasstop.draw(win)

    # creating the textbook with instructions
    textbox = Textbox()
    textbox.box.draw(win)
    textbox.message.draw(win)

# --------------------------Creating Animal Instances at Random Points----------------------------
    # bunny instance, drawing each of the bunny shapes
    bun_x = randrange(0, 1000)
    bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
    bun = Bunny(bun_x, bun_y, True)
    bun.bunear1.draw(win)
    bun.bunear2.draw(win)
    bun.buntail.draw(win)
    bun.bunbody.draw(win)
    bun.bun.draw(win)

    # fox instance, drawing each of the fox shapes
    fox_x = randrange(0, 1000)
    fox_y = 100
    fox = Fox(fox_x, fox_y, True)
    fox.fox.draw(win)
    fox.foxbody.draw(win)
    fox.foxear1.draw(win)
    fox.foxear2.draw(win)
    fox.foxtail.draw(win)
    fox.foxnose.draw(win)

    # eagle instance, drawing each of the eagle shapes
    eagle_x = randrange(0, 50)
    eagle_y = 400 * sin((1/90) * eagle_x + 18) + 350
    eagle = Eagle(eagle_x, eagle_y, True)
    eagle.eaglebody.draw(win)
    eagle.eaglewing1.draw(win)
    eagle.eaglewing2.draw(win)
    eagle.eagle.draw(win)
    eagle.eaglebeak.draw(win)

    # ---------Creating object lists for when there are more than one of each animal (being duplicated) ----------
    # bunny shapes lists, current list for each animal is initialized with starting animal
    bunny_list = [bun]
    bunny_body_list = [bun.bunbody]
    bunny_ear1_list = [bun.bunear1]
    bunny_ear2_list = [bun.bunear2]
    bunny_tail_list = [bun.buntail]

    # fox shapes lists
    fox_list = [fox]
    fox_body_list = [fox.foxbody]
    fox_ear1_list = [fox.foxear1]
    fox_ear2_list = [fox.foxear2]
    fox_tail_list = [fox.foxtail]
    fox_nose_list = [fox.foxnose]

    # eagle shapes lists
    eagle_list = [eagle]
    eagle_body_list = [eagle.eaglebody]
    eagle_wing1_list = [eagle.eaglewing1]
    eagle_wing2_list = [eagle.eaglewing2]
    eagle_beak_list = [eagle.eaglebeak]

    # grass shapes list, initialized with starting grass shapes
    grass_list = [grass]
    grass_top_list = [grass.grasstop]

    #each of the main animals are combined into a list
    animal_list = bunny_list + fox_list + eagle_list

    # ----------------------------------------------------------------------------------------------
    #                         Main While Loop for Interactions and Movements
    # ----------------------------------------------------------------------------------------------
    # setting clicking key equal to variable clickPoint
    clickPoint = win.checkKey()

    # while key 'q' is not pressed, main while loop continues
    while clickPoint != 'q':
        if clickPoint != "":
            print(clickPoint)

        # object slopes for movement method
        bun_slope = (18 * pi * cos((3 * pi * bun_x) / 1000) *
                     sin((3 * pi * bun_x) / 1000))/(5 * abs(sin((3 * pi * bun_x) / 1000)))
        fox_slope = 0
        eagle_slope = (150 * cos((eagle_x/90) + 18))/9

    # --------------------- Eating interations  ------------------------
        # for each bunny in the bunny list, if the center of the bunny is in the range (+/-20) of the center of the grass, the bunny eats the grass causing grass to dissapear and reappear in new location
        for i in bunny_list:
            for g in grass_list:
                if i.bun.getCenter().getX() >= g.grass.getCenter().getX() - 20 and i.bun.getCenter().getX() <= g.grass.getCenter().getX() + 20:
                    g.grass.undraw()
                    g.grasstop.undraw()

                    # delete the eaten grass from the grass list
                    count = grass_list.index(g)
                    del grass_list[count]
                    del grass_top_list[count]

                    # create a new grass and append the new grass to the grass list
                    grass_x = choice(grass_choice)
                    grass = Grass(grass_x)
                    grass.grass.draw(win)
                    grass.grasstop.draw(win)
                    grass_list.append(grass)
                    grass_top_list.append(grass.grasstop)

            # when fox is in range of the bunny's head, it eats the bunny

        for f in fox_list:
            for i in bunny_list:
                if (f.fox.getCenter().getY() >= i.bun.getCenter().getY() - 60 and f.fox.getCenter().getY() <= i.bun.getCenter().getY() + 60) and (f.fox.getCenter().getX() >= i.bun.getCenter().getX() - 60 and f.fox.getCenter().getX() <= i.bun.getCenter().getX() + 60):
                    # undraw bunny
                    i.bun.undraw()
                    i.bunbody.undraw()
                    i.bunear1.undraw()
                    i.bunear2.undraw()
                    i.buntail.undraw()

                    # deleting the bunny at index i
                    count = bunny_list.index(i)
                    del bunny_list[count]
                    del bunny_body_list[count]
                    del bunny_ear1_list[count]
                    del bunny_ear2_list[count]
                    del bunny_tail_list[count]
        # when eagle is in range of fox's head, it eats the fox
        for e in eagle_list:
            for i in fox_list:
                if (e.eagle.getCenter().getY() >= i.fox.getCenter().getY() - 60 and e.eagle.getCenter().getY() <= i.fox.getCenter().getY() + 60) and (e.eagle.getCenter().getX() >= i.fox.getCenter().getX() - 60 and e.eagle.getCenter().getX() <= i.fox.getCenter().getX() + 60):
                    # undraw fox
                    i.fox.undraw()
                    i.foxbody.undraw()
                    i.foxear1.undraw()
                    i.foxear2.undraw()
                    i.foxtail.undraw()
                    i.foxnose.undraw()

                    # deleting the fox at index i
                    count = fox_list.index(i)
                    del fox_list[count]
                    del fox_body_list[count]
                    del fox_ear1_list[count]
                    del fox_ear2_list[count]
                    del fox_tail_list[count]
                    del fox_nose_list[count]

    # -------- When the mouse click falls into a certain range in the animal's head, the object is undrawn --------
        # checking what point at which the mouse was clicked
        point = win.checkMouse()
        if point != None:
            for i in bunny_list:
                # if clicked within range of bunny's head, the bunny is deleted
                if (point.getY() >= i.bun.getCenter().getY() - 60 and point.getY() <= i.bun.getCenter().getY() + 60) and (point.getX() >= i.bun.getCenter().getX() - 60 and point.getX() <= i.bun.getCenter().getX() + 60):
                    # undraw bunny
                    i.bun.undraw()
                    i.bunbody.undraw()
                    i.bunear1.undraw()
                    i.bunear2.undraw()
                    i.buntail.undraw()

                    # delete the bunny that is at index i (which clone is clicked)
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
                    count2 = grass_list.index(i)
                    del grass_list[count2]
                    del grass_top_list[count2]

        # ----------- Adding animals by clicking a key on the keyboard. 'b' for bunny, 'f' for fox, 'e' for eagle, and g'g' for grass ------------
        # Bunny duplication if 'b' is clicked on the keyboard
        if clickPoint == 'b':
            bun_x = randrange(0, 1000)
            bun_y = 10 * abs(40 * sin((3 * pi/1000) * bun_x)) + 40
            bun = Bunny(bun_x, bun_y, True)
            bun.bunbody.draw(win)
            bun.bunear1.draw(win)
            bun.bunear2.draw(win)
            bun.buntail.draw(win)
            bun.bun.draw(win)
            # appending new bunny to the bunny list
            bunny_list.append(bun)
            bunny_body_list.append(bun.bunbody)
            bunny_ear1_list.append(bun.bunear1)
            bunny_ear2_list.append(bun.bunear2)
            bunny_tail_list.append(bun.buntail)

        # Fox duplication if 'f' is clicked on the keyboard
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
            # appending new fox to the fox list
            fox_list.append(fox)
            fox_body_list.append(fox.foxbody)
            fox_ear1_list.append(fox.foxear1)
            fox_ear2_list.append(fox.foxear2)
            fox_tail_list.append(fox.foxtail)
            fox_nose_list.append(fox.foxnose)

        # Eagle duplication if 'e' is clicked on the keyboard
        if clickPoint == 'e':
            eagle_x = randrange(0, 100)
            eagle_y = 10 * abs(40 * sin((3 * pi/1000) * eagle_x)) + 40
            eagle = Eagle(eagle_x, eagle_y, True)
            eagle.eaglebody.draw(win)
            eagle.eaglewing1.draw(win)
            eagle.eaglewing2.draw(win)
            eagle.eagle.draw(win)
            eagle.eaglebeak.draw(win)
            # appending new eagle to the eagle list
            eagle_list.append(eagle)
            eagle_body_list.append(eagle.eaglebody)
            eagle_wing1_list.append(eagle.eaglewing1)
            eagle_wing2_list.append(eagle.eaglewing2)
            eagle_beak_list.append(eagle.eaglebeak)

        # Grass duplication if 'g' is clicked on the keyboard
        if clickPoint == 'g':
            grass_choice = [0, 1000/3, 2000/3, 1000]
            grass_x = choice(grass_choice)
            grass = Grass(grass_x)
            grass.grass.draw(win)
            grass.grasstop.draw(win)
            # appending new grass to the grass list
            grass_list.append(grass)
            grass_top_list.append(grass.grasstop)

        update(35)
        #animal list is updated here
        animal_list = bunny_list+fox_list+eagle_list

    # -------- REVISED Animal movements --------
    #For each animal in the list, the animal moves according to its slope
        for animal in animal_list:
            animal.move1()

        clickPoint = win.checkKey()

# --------------------------------------------------------------------------
#                               CLASSES
# --------------------------------------------------------------------------
# create class Ground, and fill Line shape in with light green

class Ground:
    def __init__(self):
        self.ground = Line(Point(0, 30), Point(1000, 30))
        self.ground.setOutline("lightgreen")
        self.ground.setWidth(60)

# create class Textbox and input message and formatting

class Textbox:
    def __init__(self):
        self.box = Rectangle(Point(670, 770), Point(930, 970))
        self.message = Text(Point(800, 880), '''Instructions:
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

# create class Grass at given random x coordinate (within 3 possible choices) and y coordinate set to 0

class Grass:
    def __init__(self, grass_x):
        self.grass_x = grass_x
        self.y = 0
        self.grass = Circle(Point(grass_x, self.y), 50)
        self.grass.setFill("forest green")
        # created grass top for shape, however kept circle since the movement of the polygon is based on the movement of
        # the circle on the coordinate plane
        self.grasstop = Polygon(Point(self.grass_x, 90), Point(
            self.grass_x + 60, 0), Point(self.grass_x - 60, 0))
        self.grasstop.setFill("forest green")

# create class Bunny at given (random) x and y coordinate position, and initialize direction "right" to be True
# "right" is a given parameter bc bunny changes directions if it hits the edge of the window

class Bunny:
    def __init__(self, bun_x, bun_y, right):
        self.right = right
        self.x = bun_x
        self.y = bun_y
        self.bunear1 = Oval(Point(self.x - 5, self.y + 140),
                            Point(self.x - 45, self.y + 40))
        self.bunear1.setFill("pink")
        self.bunear2 = Oval(Point(self.x + 45, self.y + 140),
                            Point(self.x + 5, self.y + 40))
        self.bunear2.setFill("pink")
        self.bunbody = Circle(Point(self.x, self.y - 90), 60)
        self.bunbody.setFill("pink")
        self.bun = Circle(Point(self.x, self.y), 50)
        self.bun.setFill("pink")
        self.buntail = Circle(Point(self.x + 60, self.y - 90), 20)
        self.buntail.setFill("white")

    # method to move bunny, either right or left depending on whether "right" is True or False
    # bun slope is it's dx, dependant on the given equation of the sin wave on the coordinate plane
    # REVISED: we made a move function for each animal to decrease the number of code 

    def move_b(self, x, slope):
        self.x += x
        self.bunear1.move(x, slope)
        self.bunear2.move(x, slope)
        self.bunbody.move(x, slope)
        self.bun.move(x, slope)
        self.buntail.move(x, slope)

    def move1(self):
        self.bun_slope = (18 * pi * cos((3 * pi * self.x) / 1000) * sin((3 * pi * self.x) / 1000))/(5 * abs(sin((3 * pi * self.x) / 1000)))
        # if bunny hits right edge, it moves left
        if self.x > 1000:
            self.right = False
        # if bunny hits left edge of window, it moves right
        elif self.x < 10:
            self.right = True
        # because parameter right = True, bunny moves right
        if self.right:
            self.move_b(3, self.bun_slope)
        # becase parameter right = False, bunny moves left
        else:
            self.move_b(-3, -self.bun_slope)

# create class Fox at given (random) x poisiton, constant y position, and initialize "right2" to be True

class Fox:
    def __init__(self, fox_x, fox_y, right2):
        self.right2 = right2
        self.x = fox_x
        self.y = fox_y
        self.fox = Circle(Point(self.x, self.y), 50)
        self.fox.setFill("coral")
        self.foxbody = Circle(Point(self.x, self.y-90), 50)
        self.foxbody.setFill("coral")
        self.foxear1 = Polygon(Point(self.x-50, self.y + 20), Point(self.x-90, self.y+70), Point(self.x - 20, self.y+50))
        self.foxear1.setFill("coral")
        self.foxear2 = Polygon(Point(self.x+50, self.y + 20), Point(self.x+90, self.y+70), Point(self.x + 20, self.y+50))
        self.foxear2.setFill("coral")
        self.foxtail = Polygon(Point(self.x + 50, self.y - 90), Point(self.x + 150, self.y - 30), Point(self.x + 90, self.y - 100))
        self.foxtail.setFill("coral")
        self.foxnose = Polygon(Point(self.x, self.y - 10), Point(self.x + 10, self.y), Point(self.x - 10, self.y))
        self.foxnose.setFill("black")

    def move_f(self, x):
        self.x += x
        self.fox.move(x, 0)
        self.foxbody.move(x, 0)
        self.foxear1.move(x, 0)
        self.foxear2.move(x, 0)
        self.foxtail.move(x, 0)
        self.foxnose.move(x, 0)

    # fox slope is 0 since it moves in horizontal path, movement based on edges similar logic to bunny movement
    def move1(self):
        # move left
        if self.x > 1000:
            self.right2 = False
        # move right
        elif self.x < 0:
            self.right2 = True
        # because right = True, move right
        if self.right2:
            self.move_f(15)
        # because right = False, move left
        else:
            self.move_f(-15)

# create class Eagle at given (random) x coordinate and corresponding y coordinate, initialize right3 to be True

class Eagle:
    def __init__(self, eagle_x, eagle_y, right3):
        self.right3 = right3
        self.x = eagle_x
        self.y = eagle_y
        self.eagle = Circle(Point(self.x, self.y), 50)
        self.eagle.setFill("white")
        self.eaglebody = Circle(Point(self.x, self.y-90), 50)
        self.eaglewing1 = Polygon(Point(self.x + 10, self.y - 40), Point(
            self.x + 150, self.y+30), Point(self.x + 110, self.y - 40))
        self.eaglewing2 = Polygon(Point(self.x - 10, self.y - 40), Point(
            self.x - 150, self.y+30), Point(self.x - 110, self.y - 40))
        self.eaglebeak = Polygon(
            Point(self.x-20, self.y), Point(self.x+20, self.y), Point(self.x, self.y-25))
        self.eaglebeak.setFill("yellow")
        self.eaglebody.setFill("peru")
        self.eaglewing1.setFill("peru")
        self.eaglewing2.setFill("peru")
    # eagle movement method based on same logic as other animals, eagle slope representing dx of given equation

    def move_e(self, x, slope):
        self.x += x
        self.eagle.move(x, slope)
        self.eaglebody.move(x, slope)
        self.eaglewing1.move(x, slope)
        self.eaglewing2.move(x, slope)
        self.eaglebeak.move(x, slope)

    def move1(self):
        self.eagle_slope = (150 * cos((self.x/90) + 18))/9
        # move left
        if self.x > 1000:
            self.right3 = False
        # move right
        elif self.x < 0:
            self.right3 = True
        # because right = True, move right
        if self.right3:
            self.move_e(5, self.eagle_slope)
        # because right = False, move left
        else:
            self.move_e(-5, -self.eagle_slope)


if __name__ == '__main__':
    main()
