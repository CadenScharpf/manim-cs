from big_ol_pile_of_manim_imports import *
from my_library.animation.transformations import *
import os
import pyclbr


####################################################
# -ArrayElement
# -Creates a single array element with a displayable
#  value. 
# -Accepts: 
#   (1) Positional argument for: 'key'
#   (?) Arbitrary arguments for: 'color', 'buff',
#       'opacity'...etc
# ####################################################
class ArrayElement(SingleStringTexMobject):

    def __init__(self, key, **kwargs):
        #Instance variables
        CONFIG = {
            "default_color" : WHITE,
            "buff" : .5,
            "opacity" : .75
         }
        digest_config(self, kwargs)
        assert(isinstance(key, str))
        self.key = key
        super().__init__(key, **kwargs)

        #background rectangle
        self.add_background_rectangle(self.default_color, self.buff, self.opacity)

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

    # Color 
    def set_color(self, color, family=True):
        """
        Condition is function which takes in one arguments, (x, y, z).
        Here it just recurses to submobjects, but in subclasses this
        should be further implemented based on the the inner workings
        of color
        """
        if family:
            for submob in self.submobjects:
                if not isinstance(submob, TexSymbol):
                    submob.set_color(color, family=family)
        self.color = color

        return self

    def to_original_color(self):
        self.set_color(self.default_color)
        self.color = self.default_color
        return self