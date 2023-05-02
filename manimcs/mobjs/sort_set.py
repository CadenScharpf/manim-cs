import random
from manim import VGroup, Square, Mobject, Tex

from .sortable_mobject import IntegerSortableMObject


class SortSet(VGroup):
    def __init__(self, *mobjects, **kwargs):
        super().__init__(*mobjects, **kwargs)
        self.mobjects = mobjects
        self.arrange(buff=0.5).center()
    
    def __init__(self, **kwargs):
        super().__init__(*[IntegerSortableMObject(random.randint(1, 100)) for i in range(3)], **kwargs)
        self.arrange(buff=0.5).center()
    def __init__(self, values, **kwargs):
        super().__init__(*[IntegerSortableMObject(value) for value in values], **kwargs)
        self.arrange(buff=0.5).center()

    def swap(self, i, j):
        self.mobjects[i], self.mobjects[j] = self.mobjects[j], self.mobjects[i]
        self.arrange()
        return self