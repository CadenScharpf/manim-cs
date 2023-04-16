from manim import *

class AppleSVGMobject(SVGMobject):
    CONFIG = {
        "stroke_color": WHITE,
        "stroke_width": 0,
        "fill_opacity": 1,
        "height": 3
    }
    def __init__(self, value, **kwargs):
        svg_file = "../../assets/apple.svg"
        if(value <= 0): value = 3
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)