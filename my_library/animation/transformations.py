from manimlib.animation.transform import ApplyMethod

# Color
class FadeTo(ApplyMethod):
    def __init__(self, 
    ArrayElement, color, **kwargs):
        ApplyMethod.__init__(self, ArrayElement.set_color, color, **kwargs)

class FadeToOrigionalColor(ApplyMethod):
    def __init__(self, ArrayElement, **kwargs):
        ApplyMethod.__init__(self, ArrayElement.to_original_color, **kwargs)

class Fade(ApplyMethod):
   def __init__(self, ArrayElement, **kwargs):
        ApplyMethod.__init__(self, ArrayElement.fade, **kwargs)

class Brighten(ApplyMethod):
   def __init__(self, ArrayElement, **kwargs):
        ApplyMethod.__init__(self, ArrayElement.brighten, **kwargs)