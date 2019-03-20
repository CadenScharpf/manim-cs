from big_ol_pile_of_manim_imports import *
from big_ol_pile_of_caden_imports import *
from my_library.array.array import ArrayElement
import os
import pyclbr

class Array(Mobject):
    def __init__(self, **kwargs):
        Mobject.__init__(self, **kwargs)

        

# Generates an onscreen array element to be sorted
def get_array_element(value): 
    result = ArrayElement(value, .5)
    return result

"""
def construct(self): 
    self.introduce_element_group()
    self.introduce_labels()
    self.initialize_counters()

def introduce_element_group(self):
    self.element_group = self.get_line_group(self.start_x)

def introduce_labels(self):

def initialize_counter(self):

def get_element_group(self):

def get_labels(self)
"""




