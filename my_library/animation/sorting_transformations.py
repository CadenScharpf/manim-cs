from manimlib.animation.transform import Transform
from manimlib.animation.transform import ApplyMethod

class MyFadeToColor(ApplyMethod):
    def __init__(self, mobject, color, **kwargs):
        super().__init__(mobject.set_color, color, **kwargs)