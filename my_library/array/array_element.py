from big_ol_pile_of_manim_imports import *
from my_library.animation.sorting_transformations import *
import os
import pyclbr

####################################################
# -ArrayElement
# -Creates a single array element with a displayable
#  value. 
# -Accepts: 
#   (1) Positional argument for: 'key'
#   (?) Arbitrary arguments for: 'default_color', 'buff',
#       'opacity'...etc
# ####################################################
class ArrayElement(SingleStringTexMobject):
    CONFIG = {
        "key" : 0,
        "default_color" : BLACK,
        "buff" : SMALL_BUFF,
        "opacity" : .75
    }
    def __init__(self, key, **kwargs):
        digest_config(self, kwargs)
        self.styles = {
            "color" : self.default_color,
            "buff" : self.buff, 
            "opacity" : self.opacity,
        }
        assert(isinstance(key, str))
        self.key = key
        super().__init__(key, **kwargs)

    # Background rectangle
    def add_background_rectangle(self, color, buff, opacity=0.75, **kwargs):
 
        from manimlib.mobject.shape_matchers import BackgroundRectangle
        self.background_rectangle = BackgroundRectangle(
            self, color=color,
            buff = buff,
            fill_opacity=opacity,
            **kwargs
        )
        self.add_to_back(self.background_rectangle)
        return self

    def add_background_rectangle_to_submobjects(self, **kwargs):
        for submobject in self.submobjects:
            submobject.add_background_rectangle(**kwargs)
        return self

    def add_background_rectangle_to_family_members_with_points(self, **kwargs):
        for mob in self.family_members_with_points():
            mob.add_background_rectangle(**kwargs)
        return self
