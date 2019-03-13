from big_ol_pile_of_manim_imports import *
import os
import pyclbr

class ArrayElement(SingleStringTexMobject):
    CONFIG = {
        "value" : 0,
        "color" : WHITE,
        "width" : 1,
    }
    def __init__(self, value, color = WHITE, width = 1:
        SingleStringTexMobject.__init__(self, value)
        self.add_element_enclosure(self, 1, buff=1)


    def add_element_enclosure(self, buffer, color=BLACK, opacity=0.75, **kwargs):
        from manimlib.mobject.shape_matchers import BackgroundRectangle
        self.background_rectangle = BackgroundRectangle(
            self, color=color,
            fill_opacity=opacity,
            **kwargs
        )
        self.add_to_back(self.background_rectangle)
        return self
        


