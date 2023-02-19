"""Classe of 3D objects"""
###########################
#EXIT CODES : 
#1 : Argument error with the arg "id_"      (object3D file)
#2 : Argument error : you don't use the good mode name.     (screen file)
###########################

class Object3D(object):
    def __init__(self, points, color, id_='DO NOT TOUCH IT !'):
        """It is a class for create other 3D objects.
        Arguments : 
        - points : list of tuples with 3 coord.
        - id : the id is attributed by the Screen class. DO NOT TOUCH, exceept you know what you are doing !"""
        self.list_points = points
        self.list_edges = []
        self.list_faces = []
        self.list_edges2d = []
        self.list_faces2d = []
        self.color = color
        if id_ == "DO NOT TOUCH IT !":
            raise AttributeError("Sorry, but you must give this argument (id_). For it, you have to use Screen.get_id(), it gener id.")
            exit(1)
        self.id_ = id_

    def __repr__(self):
        print("""
        ------------------------------------------------------
        3D object with id {0}
        ----------- Points -------------""".format(self.id_))
        for j, i in enumerate(self.list_points):
            print(str(j+1) + " : " + i.__repr__())
        print("----------- Edges -------------")
        for j, i in enumerate(self.list_edges):
            print(str(j+1) + " : " + i.__repr__())
        print("----------- Faces -------------")
        for j, i in enumerate(self.list_faces):
            print(str(j+1) + " : " + i.__repr__())
        print("------------------------------------------------------\n")


    def get(self):
        """Return the coords of the points.
        """
        return (self.list_edges, self.list_faces)

    def create_edge(self, point1, point2):
        """Create a new edge.
        Arguments :
        - point1 : The first point.
        - point2 : the second point."""

        return (point1, point2)

    def create_face(self, points, skin=("color", "blue")):
        """Create a new face.
        Arguments : 
        - points : a list of points
        - a tuple with the type of the skin of the face, and the skin. Default : type:color and skin:blue."""

        return (points, skin)


class Cube(Object3D):
    def __init__(self, points, color, id_='DO NOT TOUCH IT !', skin=None):
        """This class from Object3d allow to create an object like a cube, with : 
        - 8 edges
        - 8 points
        - 6 faces."""
        super(Cube, self).__init__(points, color, id_)
        self.skin = skin
        #Check if there are 8 points, else return an error : a cube have 8 points, edges and 6 faces.
        if not(len(points) == 8):
            raise AttributeError("A cube must have 8 points ! For create an other object, use Object3d !")
        
        #Here we create all the edges of the cube, and add them to the list.
        x = self.list_points
        for i, j in enumerate(x):
            self.list_edges.append(self.create_edge(self.list_points[i-1], self.list_points[i]))
        
        self.list_edges.append(self.create_edge(self.list_points[7-1], self.list_points[4-1]))
        self.list_edges.append(self.create_edge(self.list_points[7-1], self.list_points[2-1]))
        self.list_edges.append(self.create_edge(self.list_points[6-1], self.list_points[1-1]))
        self.list_edges.append(self.create_edge(self.list_points[7-1], self.list_points[4-1]))
        self.list_edges.append(self.create_edge(self.list_points[0-1], self.list_points[5-1]))
        self.list_edges.append(self.create_edge(self.list_points[0-1], self.list_points[3-1]))

        #Here we create all the faces of the cube, and add them to the list.

        if self.skin == None:
            self.list_faces.append(self.create_face([self.list_points[0-1], self.list_points[1-1], self.list_points[2-1], self.list_points[3-1]]))
            self.list_faces.append(self.create_face([self.list_points[4-1], self.list_points[5-1], self.list_points[6-1], self.list_points[7-1]]))
            self.list_faces.append(self.create_face([self.list_points[0-1], self.list_points[1-1], self.list_points[6-1], self.list_points[5-1]]))
            self.list_faces.append(self.create_face([self.list_points[0-1], self.list_points[3-1], self.list_points[5-1], self.list_points[6-1]]))
            self.list_faces.append(self.create_face([self.list_points[2-1], self.list_points[3-1], self.list_points[4-1], self.list_points[7-1]]))
            self.list_faces.append(self.create_face([self.list_points[1-1], self.list_points[2-1], self.list_points[7-1], self.list_points[6-1]]))

        else:       #the same but with the selected tuple for the skin
            self.list_faces.append(self.create_face([self.list_points[0-1], self.list_points[1-1], self.list_points[2-1], self.list_points[3-1]], self.skin))
            self.list_faces.append(self.create_face([self.list_points[4-1], self.list_points[5-1], self.list_points[6-1], self.list_points[7-1]], self.skin))
            self.list_faces.append(self.create_face([self.list_points[0-1], self.list_points[1-1], self.list_points[6-1], self.list_points[5-1]], self.skin))
            self.list_faces.append(self.create_face([self.list_points[0-1], self.list_points[3-1], self.list_points[5-1], self.list_points[6-1]], self.skin))
            self.list_faces.append(self.create_face([self.list_points[2-1], self.list_points[3-1], self.list_points[4-1], self.list_points[7-1]], self.skin))
            self.list_faces.append(self.create_face([self.list_points[1-1], self.list_points[2-1], self.list_points[7-1], self.list_points[6-1]], self.skin))
        