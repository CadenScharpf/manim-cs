from big_ol_pile_of_manim_imports import *
from my_library.array.array_element import ArrayElement
import os
import pyclbr

####################################################
# - 'Array'
# - Generates a centered array of ArrayElements given
#   a string array of element keys
# - Accepts: 
#   (1) Positional argument for: 'key_array'
#   (?) Arbitrary arguments for: 'default_color, 
#       'buff', opacity', 'j_color', and 'i_color'
#####################################################
class Array(Mobject):
    CONFIG = {
        "default_color" : WHITE,
        "buff" : MED_LARGE_BUFF, 
        "opacity" : .75,

        "i_color" : BLUE,
        "j_color" : YELLOW
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

# Generate element array
def get_element_list(self, *key_array, **styles):
    print("Generating array...")
    print(key_array)
    element_list = list()
    for key in key_array:
        print("Added " + str(key) + " to the Array")

        element_list.append(ArrayElement(str(key), **styles))
    return element_list

# Swap
def swap(element):
    element.move_to(UP)
