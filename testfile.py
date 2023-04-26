"""Test file of the librairie. Use for :
--> test it
--> understand how it run
--> debug it
!!! It isn't callable !!!"""
from screen import *
from object3D import *

cube_points = [
    (1, 1, 1),  # top right front
    (-1, 1, 1),  # top left front
    (-1, -1, 1),  # bottom left front
    (1, -1, 1),  # bottom right front
    (1, 1, -1),  # top right back
    (-1, 1, -1),  # top left back
    (-1, -1, -1),  # bottom left back
    (1, -1, -1)]  # bottom right back

if __name__ == "__main__":
    module = Screen(1200, 500, "test")
    a = object3D.Cube(cube_points, color="blue", id_=module.get_id())
    module.add_object(a)
    x = input("x : ")
    y = input("y : ")
    module.rotate_x = x
    module.rotate_y = y
    module.modify_zoom(0.001)
    module.allow_move()
    module.allow_zoom()
    module.addquitbutton("EXIT")
    #module.set_zoom(5)
    module.build()
    module.mainloop()