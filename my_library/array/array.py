from big_ol_pile_of_manim_imports import *
from my_library.array.array_element import ArrayElement
import os
import pyclbr

####################################################
# - 'Array'
# - Generates a centered array of ArrayElements given
#   a string array of element keys
# - Accepts: 
#   (1) Positional array argument for: 'key_array'
#   (?) Arbitrary arguments for: 'default_color'(hex), 
#       'buff'(int), 'opacity'(double: 0<=opacity<=1), 
#       'position_color(hex)', and 'idx_color(hex)'
#####################################################
class Array(Mobject):
    CONFIG = {
        "default_color" : WHITE,
        "buff" : MED_LARGE_BUFF, 
        "opacity" : .75,

        "idx_color" : BLUE,
        "position_color" : YELLOW
    }
    def __init__(self, *key_array, **kwargs):
        print(key_array)
        if not all([isinstance(key, str) for key in key_array]):
            raise Exception("All keys must be of type string")
        digest_config(self, kwargs)

        self.element_styles = {
            "default_color" : self.default_color,
            "buff" : self.buff, 
            "opacity" : self.opacity,
        }

        self.element_list = get_element_list(self, *key_array, **self.element_styles)
        super().__init__(**kwargs)
        self.add(*self.element_list)
        self.add_background_rectangle_to_submobjects(color=self.default_color,**self.element_styles)
        self.arrange()
        print(self.element_list)

        # Swap
    def swap(self, element_idx):
        ApplyMethod(self.element_list[element_idx].move_to(UP))

# Generate array_element list
def get_element_list(self, *key_array, **styles):
    print("Generating array...")
    print(key_array)
    element_list = list()
    for key in key_array:
        print("Added " + str(key) + " to the Array")

        element_list.append(ArrayElement(str(key), **styles))
    return element_list

