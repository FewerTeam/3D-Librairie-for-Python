"""3D librairie"""
###########################
#EXIT CODES : 
#1 : Argument error with the arg "id_"      (object3D file)
#2 : Argument error : you don't use the good mode name.
###########################
#IMPORT
from tkinter import *
import object3D     #Dev in the project

class Screen(object):
    """Screen is a class who create a Tk screen, and who can have 3d objects."""
    def __init__(self, width, height, title, background="white", type3d="num", lock=True, showgrid=True):
        """
        Initialing the class, and the screen.
        Arguments : 
        - width : the width of the screen
        - height : the height of the screen
        - background : the color of the background (default "white")
        - type3d : the type of the file (game, value...) (accepted value=["game", "num"], take "num" in default.)
        - lock : define if we can move the view or not (default True)
        - showgrid : define if we show the grid of the 3 axis (default True).
        - title : the title of the screen.
        """
        self.width = width
        self.height = height
        self.title = title
        self.bc = background
        self.type = type3d
        self.lock = lock
        self.showgrid = showgrid

        #Spectator values :
        self.x = 0
        self.y = 0
        self.z = 0

        ############

        self.orient_y = 0
        self.orient_z = 0

        self.MAX_Z_ORIENT = (-45, 45)

        self.root = Tk()
        self.root.title(self.title)

        self.screen_f = Frame(self.root)
        self.screen_f.pack()

        self.screen = Canvas(self.screen_f, width=self.width, height=self.height, bg=self.bc)
        self.screen.pack()

        self.quitbtnFrame = Frame(self.root)
        self.quitbtnFrame.pack()
        self.quitbtn = None

        self.list_object = []

    def addquitbutton(self, text):
        """Show the quit button in the screen, and ad text to it."""
        if self.quitbtn == None:
            self.quitbtn = Button(self.quitbtnFrame, text=text, command=self.root.destroy)
            self.quitbtn.pack()
            return 1
        else:
            return 0

    def removequitbutton(self):
        """Remove the quit button"""
        if not(self.quitbtn == None):
            self.quitbtn.destroy()
            return 1
        else:
            return 0

    def showgridf(self):
        if self.showgrid == False:
            self.showgrid = True

    def allow_move(self):
        self.screen.bind("<B2-Motion>", self.move)
        self.last_x = 0
        self.last_y = 0

    def move(self, event):
        x = event.x
        y = event.y
        #Determine the type of the event
        if x < self.last_x:
            etx = "Left"
        elif x > self.last_x:
            etx = "Right"
        else:
            etx = None
        if y < self.last_y:
            ety = "Up"
        elif y > self.last_y:
            ety = "Down"
        else:
            ety = None
        
        #Move
        if etx == "Left":
            v = self.last_x - x
            self.move_l(v)
        if etx == "Right":
            v = x - self.last_x
            self.move_r(v)
        if ety == "Up":
            v = self.last_y - y
            self.move_u(v)
        if ety == "Down":
            v = y - self.last_y
            self.move_d(v)

        self.last_x = x
        self.last_y = y

    
    def move_l(self, value):
        print("I go to the left with value {0}".format(value))

    def move_r(self, value):
        print("I go to the right with value {0}".format(value))

    def move_u(self, value):
        print("I go to the up with value {0}".format(value))

    def move_d(self, value):
        print("I go to the down with value {0}".format(value))

    def mainloop(self):
        mainloop()

    def add_object(self, object3d):
        """Add an object to the screen.
        Arguement : 
        - object3d : the 3D object.
        """
        self.list_object.append(object3d)
        self.reload()
        

    def reload(self):
        """Reload the Screen."""
        self.list_points = []
        self.priority = []
        self.set_priority()
        self.screen.destroy()
        self.screen = Canvas(self.screen_f, width=self.width, height=self.height, bg=self.bc)
        self.screen.pack()

        #Enumerating the list of objects and giving their points list
        for i in self.list_object:
            #i = one object
            x = i.get()
            #giving i's list of tuple
            for j in x:
                #j = a tuple
                #Checking if the tuple has 3 items
                if not(len(x) == 2):
                    raise ValueError("A tuple hasn't got 3 items, but less or more.")
                
                
        self.build()

    def set_priority(self):
        """Give the priority of visual (what I show or not)"""
        pass

    def convertise(self, point3d, perspective="//"):
        """Convertise points 3d to a points 2d.
        Arguments:
        - point 3d : the point 3d (tuple of the 3 axis)
        return the point 2d
        - perspective : the perspective used. Can be "//" (parallel) or "()" (humain perspective). "//" is the default value."""
        if perspective == "//":
            return self._convertise_parallel(point3d)
        elif perspective == "()":
            return self._convertise_humain(point3d)
        else:
            raise Exception("This mode doesn't exist, or isn't anvaible. Please check the doc.")
            exit(2)
        

    def _convertise_parallel(self, point3d):
        """Convertise a 3d point to a 2d point with the rules of the isometric perspective.
        Arguments : 
        - point3d : the point3d who will be convertised."""

    def _convertise_humain(self, point3d):
        """Convertise a 3d point to a 2d point with the rules of the "humain" perspective.
        Arguments : 
        - point3d : the point3d who will be convertised."""


    def build(self):
        """Build all the 3d object into the screen"""
        #Enumerating the list of objects and giving their points list
        for i in self.list_object:
            #i = one object
            x = i.get()
            #giving i's list of tuple
            for j in x:
                #j = a tuple
                pass

        self.screen.update()
        self.root.update()

#MAIN
if __name__ == "__main__":
    print("DO NOT USE IT LIKE THAT ! It is a module of a librairie !")
    module = Screen(200, 200, "yo le test")
    module.allow_move()
    module.addquitbutton("EXIT")
    module.mainloop()