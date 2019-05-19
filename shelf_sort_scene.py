from big_ol_pile_of_manim_imports import *
from my_library.array.array import *
from my_library.array.array_element import *
from my_library.animation.transformations import *
import os
import pyclbr

# Default Array Configuration
ARRAY_CONFIG = {
    "default_color" : BLUE,
    "buff" : MED_LARGE_BUFF,
    "opacity" : .75
    }
# Index Color Configuration
IDX_COLOR = YELLOW_C
SUBIDX_COLOR = LIGHT_GREY

# Array Configuration Variables
keys = ("11", "15", "12", "16", "14", "17")

class ShelfSortScene(Scene):
    def construct(self):

        # Initialize Array Object
        array = Array(*keys, **ARRAY_CONFIG)

        #Show Array
        self.play(ShowCreation(array)) 
        self.selection_sort(array)

    def selection_sort(self, array):
        i = 0
        while i < len(array.element_list)-1:
            min_idx = i
            self.fade_to(array, i, IDX_COLOR)

            j = i+1
            while j < len(array.element_list):
                if int(array.element_list[j].key) < int(array.element_list[min_idx].key) and min_idx == i:
                    self.fade_to(array, i, ARRAY_CONFIG['default_color'])
                elif int(array.element_list[j].key) < int(array.element_list[min_idx].key):
                    min_idx = j
                self.flash(array, j, SUBIDX_COLOR)
                j = j+1

            if min_idx != i:
                self.swap(array, i, min_idx)
                print("ho")
            i = i+1

                
            

    def swap(self, array, elm1, elm2):
        elm1_center = array.element_list[elm1].get_center()
        elm2_center = array.element_list[elm2].get_center()
        self.play(
            array.element_list[elm1].move_to,UP*2+LEFT,
            array.element_list[elm2].move_to,UP*2+RIGHT
        )
        self.play(
            array.element_list[elm1].move_to,elm2_center,
            array.element_list[elm2].move_to,elm1_center
        )
        temp = array.element_list[elm1]
        array.element_list[elm1] = array.element_list[elm2]
        array.element_list[elm2] = temp

    def fade_to(self, array, element, color):
        self.play(FadeTo(array.element_list[element],color))

    def flash(self, array, element, color):
        old_color = array.element_list[element].default_color
        self.play(FadeTo(array.element_list[element],color))
        self.play(FadeToOrigionalColor(array.element_list[element]))

        
        
        


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