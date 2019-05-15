from manimlib.animation.transform import Transform
from manimlib.animation.transform import ApplyMethod

# Color
class FadeTo(ApplyMethod):
    def __init__(self, mobject, color, **kwargs):
        ApplyMethod.__init__(self, mobject.set_color, color, **kwargs)

class FadeToOrigionalColor(ApplyMethod):
    def __init__(self, mobject, **kwargs):
        ApplyMethod.__init__(self, mobject.to_original_color, **kwargs)
