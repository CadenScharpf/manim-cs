from big_ol_pile_of_manim_imports import *
from my_library.array.array import *
from my_library.array.array_element import *
from my_library.animation.sorting_transformations import *
import os
import pyclbr

class ShelfSortScene(Scene):
    def construct(self):

     # Array Config
        keys = ("11", "15", "12")
        styles = {
            "default_color" : BLUE,
            "buff" : MED_LARGE_BUFF,
            "opacity" : .75
        }
    # Initialize Array Object
        array = Array(*keys, **styles)
    #Show Array
        self.play(ShowCreation(array)) 
        print(array.element_list[0].key)
        print(array.element_list[1].key)
        print(array.element_list[2].key)
        self.selection_sort(array)

        # Make the softing algorithms as methods of this scene

    def selection_sort(self, array):
        for i in range(len(array.element_list)):
            self.play(FadeToColor(array.element_list[i],RED))
            

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
        temp = array.element_list[0]
        array.element_list[0] = array.element_list[1]
        array.element_list[1] = temp
        print(array.element_list[0].key)
        print(array.element_list[1].key)
        print(array.element_list[2].key)
        
        
        


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