from big_ol_pile_of_manim_imports import *
from big_ol_pile_of_caden_imports import *
from my_library.animation.sorting_transformations import *
import os
import pyclbr

####################################################
# ArrayElement object
# Creates a single array element with a displayable
# value. 
# Accepts arguments for color, buffer(width/2)
####################################################
class ArrayElement(SingleStringTexMobject):
    CONFIG = {
        "value" : 0,
        "color" : WHITE,
        "buffer" : SMALL_BUFF,
    }
    def __init__(self, value, buffer=SMALL_BUFF, color = WHITE,): # value, buffer, color = WHITE,
        self.value = value
        SingleStringTexMobject.__init__(self, value)
        self.add_element_enclosure(.5, color=color)

    # Adds the BackgroundEnclosure to mobject 'self'
    def add_element_enclosure(self, buffer, color=WHITE, opacity=0.75, **kwargs):
        self.background_rectangle = BackgroundEnclosure(
            self, buffer, color=color,
            fill_opacity=opacity,

            **kwargs
        )
        self.add_to_back(self.background_rectangle)


####################################################
# -SurroundingEnclosure class for ArrayElement
# -
# -Accepts arguments for color, buffer(width/2), and 
#  position.
####################################################
class SurroundingEnclosure(Rectangle):
    CONFIG = {
        "color": WHITE,
        "buff": SMALL_BUFF,
    }

    def __init__(self, mobject, buffer, **kwargs):
        self.buff = buffer
        digest_config(self, kwargs)
        kwargs["width"] = 2 * self.buff
        kwargs["height"] = 2 * self.buff
        Rectangle.__init__(self, **kwargs)
        print(kwargs["width"])
        self.move_to(mobject)

class BackgroundEnclosure(SurroundingRectangle):
    CONFIG = {
        "color": WHITE,
        "stroke_width": 0,
        "fill_opacity": 0.75,
        "buff": SMALL_BUFF,
    }

    def __init__(self, mobject, buffer, **kwargs):
        self.buff = buffer 
        SurroundingEnclosure.__init__(self, mobject, buffer, **kwargs)
        self.original_fill_opacity = self.fill_opacity
        
    def pointwise_become_partial(self, mobject, a, b):
        self.set_fill(opacity=b * self.original_fill_opacity)
        return self

    def set_style_data(self,
                       stroke_color=None,
                       stroke_width=None,
                       fill_color=None,
                       fill_opacity=None,
                       family=True
                       ):
        # Unchangable style, except for fill_opacity
        VMobject.set_style_data(
            self,
            stroke_color=BLACK,
            stroke_width=0,
            fill_color=BLACK,
            fill_opacity=fill_opacity
        )
        return self

    def get_fill_color(self):
        return Color(self.color)
        


