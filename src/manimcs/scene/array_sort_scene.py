from manim import Scene
from ..mobjs import SortSet

class ArraySortScene(Scene):
    def __init__(self, algorithm,elems: SortSet):
        super().__init__()
        self.algorithm = algorithm
        self.elems = elems

    def construct(self):
        self.add(self.elems)
        self.algorithm(self,self.elems)