import sys
from manim import Scene, Circle, Square, config, LEFT, RIGHT
from ..mobjs import SortSet

class ManimCSRenderer:
    def __init__(self, scene: Scene):
        self.scene = scene

    def render_scene(self):
        # Render the scene
        self.scene.render()

