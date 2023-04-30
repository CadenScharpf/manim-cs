from abc import ABC, abstractmethod
import math
from typing import TypeVar
from manim import VGroup, Square, Mobject, Tex
from matplotlib.sankey import DOWN

T = TypeVar('T', bound='SortableMobject')

class SortableMobject(ABC, VGroup):
    value = 0
    border = None
    label = None

    def __init__(self, value):
        self.value = value
        self.init_mobjects()
        super().__init__(self.border, self.label)
        

    def val(self) -> int:
        return self.value
    
    @abstractmethod
    def init_mobjects(self):
        pass

    def calculate_scalar(x, a, b):
         return -(math.log(x/3.6 + 1) / math.log(1/3.6) + a)
    
    def equals(self, op: T) -> bool:
        return True if self.value == op.val() else False
        
    def not_equals(self, op: T) -> bool:
        return True if self.value != op.val() else False
    
    """ def __eq__(self, op: T) -> bool:
        return True if self.value == op.val() else False
    def __ne__(self, op: T) -> bool:
        return True if self.value != op.val() else False """
    def __lt__(self, op: T) -> bool:
        return True if self.value < op.val() else False
    def __gt__(self, op: T) -> bool:
        return True if self.value > op.val() else False
    def __le__(self, op: T) -> bool:
        return True if self.value <= op.val() else False
    def __ge__(self, op: T) -> bool:
        return True if self.value >= op.val() else False
    """ def __hash__(self):
        return hash(self.value) """

class IntegerSortableMObject(SortableMobject):
    def __init__(self, value: int, shape=Square): 
        if(not issubclass(shape, Mobject)):
            shape=Square
            #raise ValueError("IntegerSortableMObject shape must be a subclass of Mobject")
        self.shape = shape
        super().__init__(value)

    def init_mobjects(self):
        self.border = self.shape(fill_opacity=0).scale(.5)
        self.label = Tex(str(self.val())).scale(.5)
    
class SizeSortableMobject(SortableMobject):
    def __init__(self, value: float, label: str, shape=Square): 
        if(not issubclass(shape, Mobject)):
            shape=Square
            #raise ValueError("IntegerSortableMObject shape must be a subclass of Mobject")
        self.shape = shape
        if(value <= 0):
            value = 0.1
            #raise ValueError("SizeSortableMobject value must be greater than 0")
        super().__init__()

    def init_mobjects(self):
        self.border  = self.shape(fill_opacity=1).scale(self.calcuate_scalar(self.val(), 1, 5))
        self.label = Tex(self.label).scale(2)