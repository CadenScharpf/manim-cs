from big_ol_pile_of_manim_imports import *
from my_library.array.array import *
from my_library.array.array_element import *
from my_library.animation.transformations import *
import os
import pyclbr

# Array Configuration Variables
keys = ("11", "15", "12", "16", "14", "17")

ARRAY_CONFIG = {
    "default_color" : BLUE,
    "buff" : MED_LARGE_BUFF,
    "opacity" : .75
}

class TestScenes(Scene):

    def construct(self):
        # Initialize Array Object
        array = Array(*keys, **ARRAY_CONFIG)
        #Show Array
        self.play(ShowCreation(array)) 
        self.play(Flash(array[0],GREEN))




if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'test_scenes'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("shelf_sort.py %s -l" % item.name)  #Does not play files