from big_ol_pile_of_manim_imports import *
from big_ol_pile_of_caden_imports import *
from my_library.animation.sorting_transformations import *
import os
import pyclbr

####################################################
# -ArrayElement
# -Creates a single array element with a displayable
#  value. 
# -Accepts: 
#   (1) Positional argument for: 'Key'
#   (?) Arbitrary arguments for: 'fill_color', 'buff',
#       'opacity'...etc
# ####################################################
class ArrayElement(SingleStringTexMobject):
    CONFIG = {
        "key" : 0,
        "background_color" : WHITE,
        "buff" : SMALL_BUFF,
    }
    def __init__(self, key, **kwargs):
        digest_config(self, kwargs)
        assert(isinstance(key, str))
        self.key = key
        super().__init__(key, **kwargs)
        self.add_background_rectangle(self.background_color, self.buff)

    # Background rectangle
    def add_background_rectangle(self, color, buff, opacity=0.75, **kwargs):
        # TODO, this does not behave well when the mobject has points,
        # since it gets displayed on top
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
