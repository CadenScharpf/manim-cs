from big_ol_pile_of_manim_imports import *
import os
import pyclbr

class Array(Mobject):
    CONFIG = {
        ""
    }

    def __init__(self, **kwargs):
        Mobject.__init__(self, **kwargs)

def get_array_element(value): 
    result = ArrayElement(value, .5)
    return result