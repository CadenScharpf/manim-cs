from big_ol_pile_of_manim_imports import *
from my_library.array.array import *
from my_library.animation.sorting_transformations import *
import os
import pyclbr

class SelectionSort(Scene):
    def construct(self):
        elements = list(map(ArrayElement, [
            "4", "1", "9", "7", "2", "3", "6", "8", "0"
        ]))
        
        array = Array()
        array.add(elements)
        array.arrange()
        self.add(array)
        self.play(ShowCreation(array))


if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'shelf_sort'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("shelf_sort.py %s -l" % item.name)  #Does not play files