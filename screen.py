"""3D librairie"""
###########################
#EXIT CODES : 
#1 : Argument error with the arg "id_"      (object3D file)
#2 : Argument error : you don't use the good mode name.     (screen file)
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
        self.zoom = 10
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

        self.reload()
        self.allow_move()

    
    def move_l(self, value):
        print("I go to the left with value {0}".format(value))
        self.orient_y += value

    def move_r(self, value):
        print("I go to the right with value {0}".format(value))
        self.orient_y -= value

    def move_u(self, value):
        print("I go to the up with value {0}".format(value))
        self.orient_z -= value

    def move_d(self, value):
        print("I go to the down with value {0}".format(value))
        self.orient_z += value

    def mainloop(self):
        mainloop()

    def add_object(self, object3d):
        """Add an object to the screen.
        Argument : 
        - object3d : the 3D object.
        """
        self.list_object.append(object3d)
        self.reload()
        

    def reload(self):
        """Reload the Screen."""
        self.list_points = []
        self.priority = []
        #self.set_priority()
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

        #NOTE FOR DEV : https://fr.wikipedia.org/wiki/Reconstruction_3D_%C3%A0_partir_d%27images
        """if point3d[2] == 0:
            x = point3d[0] / 2
            y = point3d[1] / 2
        else:
            x = point3d[0] * point3d[2] / 2
            y = point3d[1] * point3d[2] / 2
        return (point3d[0] * self.zoom, point3d[1] * self.zoom)"""
        return ((point3d[0] * (point3d[2] / 10)*self.zoom), 
                (point3d[1] * (point3d[2] / 10)*self.zoom))

    def _convertise_humain(self, point3d):
        """Convertise a 3d point to a 2d point with the rules of the "humain" perspective.
        Arguments : 
        - point3d : the point3d who will be convertised."""


    def build(self, mode="//"):
        """Build all the 3d object into the screen"""
        for i in self.list_object:
            #convert edges
            for j in i.list_edges:
                i.list_edges2d.append((self.convertise(j[0], mode), (self.convertise(j[1], mode))))
            #convert faces
            for j in i.list_faces:
                lst = []
                for k in j[0]:
                    lst.append(self.convertise(k, mode))
                i.list_faces2d.append((lst, j[1]))
                
            #show faces
            for j in i.list_faces2d:
                if j[1][0] == "color":
                    self.screen.create_polygon(j[0][0], j[0][1], j[0][2], j[0][3], fill=j[1][1], outline="black")

            #show edges
            """
            for j in i.list_edges2d:
                self.screen.create_line(j[0][0], j[0][1], j[1][0], j[1][1], fill="black")"""

        self.screen.update()
        self.root.update()

    def get_id(self):
        """Return a new id for a new 3D object."""
        return len(self.list_object) + 1

    def addframe(self):
        """Add a "border" to the screen"""
        p1 = self.convertise((0, 0, 0))
        p2 = self.convertise((self.width, self.height, 0))
        self.screen.create_rectangle(p1[0], p1[1], p2[0], p2[1], outline="black")

#MAIN (test)
if __name__ == "__main__":
    print("DO NOT USE IT LIKE THAT ! It is a module of a librairie !")
    module = Screen(410, 410, "yo le test")
    a = object3D.Cube([(10, 10, 10), (20, 10, 10), (20, 10, 20), (10, 10, 20), (10, 20, 20), (10, 20, 10), (20, 20, 10), (20, 20, 20)], color="blue", id_=module.get_id())
    module.add_object(a)
    module.allow_move()
    module.addframe()
    module.addquitbutton("EXIT")
    module.mainloop()