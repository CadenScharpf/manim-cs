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
    CONFIG = {
            "key": 0,
            "default_color" : WHITE,
            "color" : WHITE,
            "buff" : .5,
            "opacity" : .75
         }

    def __init__(self, key, **kwargs):
         digest_config(self, kwargs)
         assert(isinstance(key, str))
         super().__init__(key)
         if self.name is None:
            self.name = self.__class__.__name__
         assert(isinstance(key, str))
         self.key = key
         self.initialize_colors(**kwargs)

    # Init methods
    def initialize_colors(self, **kwargs):
         if 'default_color' in kwargs:
             self.default_color = Color(kwargs.get("default_color"))
             self.color = Color(kwargs.get("default_color"))
         #background rectangle
         self.add_background_rectangle(self.default_color, self.buff, self.opacity)
         return self

    # Background rectangle
    def add_background_rectangle(self, color, buff, opacity, **kwargs):
 
        from manimlib.mobject.shape_matchers import BackgroundRectangle
        self.background_rectangle = BackgroundRectangle(
            self, color=color,
            buff = buff,
            fill_opacity=.75,
            **kwargs
        )
        self.add_to_back(self.background_rectangle)
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

    def fade(self):
        from colormap import rgb2hex

        red = self.color.get_red()*255
        red = int(round(red - (red * .3)))
        green = self.color.get_green()*255
        green = int(round(green - (green * .3)))
        blue = self.color.get_blue()*255
        blue = int(round(blue - (blue * .3)))

        self.set_color(rgb2hex(red,green,blue))
        return self
    
