from screen import *
from object3D import *

if __name__ == "__main__":
    module = Screen(410, 410, "yo le test")
    a = object3D.Cube([(10, 10, 10), (20, 10, 10), (20, 10, 20), (10, 10, 20), (10, 20, 20), (10, 20, 10), (20, 20, 10), (20, 20, 20)], color="blue", id_=module.get_id())
    module.add_object(a)
    module.allow_move()
    module.addquitbutton("EXIT")
    module.set_zoom(5)
    module.build()
    module.mainloop()