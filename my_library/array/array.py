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
#   (?) Arbitrary arguments for: 'color'(hex), 
#       'buff'(width), 'opacity'(double: 0 <=
#       opacity <= 1), 
#####################################################
class Array(Mobject):
    CONFIG = {
    "default_color" : BLUE,
    "buff" : .5,
    "opacity" : .75
    }

    def __init__(self, *key_array, **kwargs):
        if not all([isinstance(key, str) for key in key_array]):
            raise Exception("All keys must be of type string")
        digest_config(self, kwargs)

        self.element_list = get_element_list(self, *key_array, **self.CONFIG)
        super().__init__(**kwargs)
        self.add(*self.element_list)
        self.arrange()

# Generate array_element list
def get_element_list(self, *key_array, **element_styles):
    print("Generating array...")
    print(key_array)
    element_list = list()
    for key in key_array:
        print("Added " + str(key) + " to the Array")

        element_list.append(ArrayElement(str(key), **element_styles))
    return element_list

