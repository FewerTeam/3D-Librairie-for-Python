"""Classe of 3D objects"""
###########################
#EXIT CODES : 
#1 : Arguemnt error with the arg "id_"
#
###########################

class Object3D(object):
    def __init__(self, points, color, id_='DO NOT TOUCH IT !'):
        """It is a class for create other 3D objects.
        Arguments : 
        - points : list of tuples with 3 coord.
        - id : the id is attributed by the Screen class. DO NOT TOUCH, exceept you know what you are doing !"""
        self.list_points = points
        self.color = color
        if id_ == "DO NOT TOUCH IT !":
            raise AttributeError("Sorry, but you must give this argument (id_). For it, you have to use Screen.get_id(), it gener id.")
            exit(1)
        self.id_ = id_

    def get(self, what="ALL"):
        """Return the coords of the points.
        Arguments :
        - what : which point return (a number or "ALL", "ALL" is default.)
        """
        if what == "ALL":
            return self.list_points
        else:
            return self.list_points[what]