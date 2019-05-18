from manimlib.animation.transform import Transform
from manimlib.animation.transform import ApplyMethod
from my_library.array.array_element import *

# Color
class FadeTo(ApplyMethod):
    def __init__(self, 
    ArrayElement, color, **kwargs):
        ApplyMethod.__init__(self, ArrayElement.set_color, color, **kwargs)

class FadeToOrigionalColor(ApplyMethod):
    def __init__(self, ArrayElement, **kwargs):
        ApplyMethod.__init__(self, ArrayElement.to_original_color, **kwargs)

class Flash(ApplyMethod):
    def __init__(self, ArrayElement, color, **kwargs):
         ApplyMethod.__init__(self, ArrayElement.flash, color, **kwargs)
         
