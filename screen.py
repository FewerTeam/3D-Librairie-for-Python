"""3D librairie"""
#IMPORT
from tkinter import *
import object3D     #Dev in the project
from Python_3D_Libs_errors import *
from math import *

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
        self.MOVE = 5
        self.width = width
        self.height = height
        self.title = title
        self.bc = background
        self.type = type3d
        self.lock = lock
        self.showgrid = showgrid
        self.zoom = 1

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

        self.screen = Canvas(self.screen_f, width=self.width, height=self.height, bg=self.bc, cursor="watch")
        self.screen.pack()

        self.move_g = Frame(self.root)
        self.move_g.pack()

        #translations

        self.move_frame = Frame(self.move_g, border=5, bg="white", cursor="fleur")
        self.move_frame.pack(side=LEFT)

        self.move_frame_up = Frame(self.move_frame)
        self.move_frame_up.pack()
        self.move_frame_middle = Frame(self.move_frame)
        self.move_frame_middle.pack()
        self.move_frame_down = Frame(self.move_frame)
        self.move_frame_down.pack()

        #zoom

        self.zoom_frame = Frame(self.move_g, border=5, bg="white", cursor="double_arrow")
        self.zoom_frame.pack(side=LEFT)

        self.quitbtnFrame = Frame(self.root)
        self.quitbtnFrame.pack()
        self.quitbtn = None

        self.list_object = []

    def __str__(self):
        for i, j in enumerate(self.list_object):
            return "Object {0} : \n{1}".format(i, j)
        if self.list_object == []:
            return "There is nothing to show..."
        
    def __repr__(self):
        for i, j in enumerate(self.list_object):
            return "Object {0} : \n{1}".format(str(i), j)
        if self.list_object == []:
            return "There is nothing to show..."
        
    def __del__(self):
        try:
            self.root.destroy()
        except:
            pass

    def project_point(self, point, camera, rotation):
        #THANKS TO CHAT OPENAI (CHAT GPT0 FOR THIS METHOD) !
        xCam, yCam, zCam = camera
        roll, pitch, yaw = rotation
        xPoint, yPoint, zPoint = point

        # Translation
        xTrans = xPoint - xCam
        yTrans = yPoint - yCam
        zTrans = zPoint - zCam

        # Rotation
        xRot = xTrans * cos(-yaw) * cos(-pitch) - yTrans * sin(-yaw) * cos(-roll) + zTrans * sin(-roll)
        yRot = xTrans * sin(-yaw) * cos(-pitch) + yTrans * cos(-yaw) * cos(-roll) + zTrans * sin(-pitch) * sin(-roll)
        zRot = -xTrans * sin(-pitch) + yTrans * sin(-roll) + zTrans * cos(-pitch) * cos(-roll)

        # Projection
        xNormalized = xRot / zRot
        yNormalized = yRot / zRot

        #
        xFinal = xNormalized
        yFinal = yNormalized

        return (xFinal*self.zoom, yFinal*self.zoom)
    
    def allow_zoom(self):
        """Allow user to move"""
        Label(self.zoom_frame, text="ZOOM", bg="white").pack()
        Button(self.zoom_frame, text="+", command=self.user_zoom_up).pack()
        Button(self.zoom_frame, text="X", command=self.reset_zoom, bg="red").pack()
        Button(self.zoom_frame, text=" - ", command=self.user_zoom_down).pack()
        self.zoom_show = Label(self.zoom_frame, text="{0} %".format(self.zoom*100), bg="white")
        self.zoom_show.pack()

    def user_zoom_up(self):
        """Add 1 to self.zoom"""
        self.modify_zoom(1)
        self.move()
        self.zoom_show.destroy()
        self.zoom_show = Label(self.zoom_frame, text="{0} %".format(self.zoom*100), bg="white")
        self.zoom_show.pack()

    def reset_zoom(self):
        """Reset the zoom factor"""
        self.zoom = 1
        self.move()
        self.zoom_show.destroy()
        self.zoom_show = Label(self.zoom_frame, text="{0} %".format(self.zoom*100), bg="white")
        self.zoom_show.pack()

    def user_zoom_down(self):
        """Remove 1 to self.zoom"""
        self.modify_zoom(-0.01)
        self.move()
        self.zoom_show.destroy()
        self.zoom_show = Label(self.zoom_frame, text="{0} %".format(self.zoom*100), bg="white")
        self.zoom_show.pack()

    def addquitbutton(self, text):
        """Show the quit button in the screen, and ad text to it."""
        if self.quitbtn == None:
            self.quitbtn = Button(self.quitbtnFrame, text=text, command=self.root.destroy, bg="red")
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
        """Allow translations"""
        # !!! movements are inversed !!! #
        Label(self.move_frame_up, text="MOVE", bg="white").pack()
        Button(self.move_frame_up, text="\u2191", command=self.move_u).pack()
        Button(self.move_frame_middle, text="\u2190", command=self.move_r).pack(side=LEFT)
        Button(self.move_frame_middle, text="X", command=self.move_reset, bg="red").pack(side=LEFT)
        Button(self.move_frame_middle, text="\u2192", command=self.move_l).pack(side=LEFT)
        Button(self.move_frame_down, text="\u2193", command=self.move_d).pack()

    def move(self):
        """DON'T CALL ME !
        Total reload for apply move"""
        self.reload()
        self.build()

    def move_reset(self):
        """Reset all move modifficators"""
        self.x = 0
        self.y = 0
        self.move()
    
    def move_l(self):
        self.x += self.MOVE
        self.move()

    def move_r(self):
        self.x -= self.MOVE
        self.move()

    def move_u(self):
        self.y -= self.MOVE
        self.move()

    def move_d(self):
        self.y += self.MOVE
        self.move()

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
        self.screen.destroy()
        self.screen = Canvas(self.screen_f, width=self.width, height=self.height, bg=self.bc, cursor="watch")
        self.screen.pack()
        #reset lists
        for i in self.list_object:
            i.list_faces2d = []
            i.list_edges2d = []

    def set_priority(self):
        """Give the priority of visual (what I show or not)"""
        ...

    def convertise(self, point3d, perspective="()"):
        """Convertise points 3d to a points 2d.
        Arguments:
        - point 3d : the point 3d (tuple of the 3 axis)
        return the point 2d
        - perspective : the perspective used. Can be "//" (parallel) or "()" (humain perspective). "//" is the default value."""
        """if perspective == "//":
            return self._convertise_parallel(point3d)
        elif perspective == "()":
            return self._convertise_humain(point3d)
        else:
            raise UnknowModeNameError("This mode doesn't exist, or isn't anvaible. Please check the doc.")
            exit(2)"""
        return self.project_point(point3d, (self.x, self.y, self.z), (self.orient_y, self.orient_z, 0))
        

    def _convertise_parallel(self, point3d):
        """Convertise a 3d point to a 2d point with the rules of the isometric perspective.
        Arguments : 
        - point3d : the point3d who will be convertised."""
        raise NotTestedCodeWarning("This method wasn't tested / coded ! Please check the version of the librairie.")

    def _convertise_humain(self, point3d):
        """Convertise a 3d point to a 2d point with the rules of the "humain" perspective.
        Arguments : 
        - point3d : the point3d who will be convertised."""
        return ((point3d[0] + point3d[2]/2)*self.zoom + self.x, 
                (point3d[1] + point3d[2]/2)*self.zoom + self.y)
    
    def set_zoom(self, zoom):
        """Modify the zoom factor.
        Arguments : 
        - zoom : the new zoom factor --> float (0 < zoom)"""
        self.zoom = zoom
        self.zoom_show.destroy()
        self.zoom_show = Label(self.zoom_frame, text="{0} %".format(self.zoom*100), bg="white")
        self.zoom_show.pack()

    def modify_zoom(self, mod):
        """Modify the zoom factor
        Arguments :
        - mod : the modificator of the zoom (float or int). It is added to Screen.zoom
        --> return Screen.zoom"""
        self.zoom += mod
        return self.zoom
        self.zoom_show.destroy()
        self.zoom_show = Label(self.zoom_frame, text="{0} %".format(self.zoom*100), bg="white")
        self.zoom_show.pack()

    def build(self, mode="()"):
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
