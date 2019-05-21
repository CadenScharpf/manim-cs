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
            "default_color" : WHITE,
            "color" : WHITE,
            "buff" : .5,
            "opacity" : .75
         }

