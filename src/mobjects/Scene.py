import os
import random
from manim import *
from sort_set import SortSet
from sortable_mobject import IntegerSortableMObject, SizeSortableMobject

current_dir = os.path.dirname(os.path.abspath(__file__))
algorithms_dir = os.path.join(current_dir, '..', 'algorithms')
sys.path.append(algorithms_dir)

from sorting import Sorting
                  
class Scene(Scene):
    def construct(self):
        # Create 10 squares and add them to a VGroup
        #arr = VGroup(*[IntegerSortableMObject() for i in range(5)])
        testElems = SortSet([3, 6, 1, 8, 1, 5, 7, 0 ]).arrange(buff=0.5).center()
        self.add(testElems)
        Sorting.insertion_sort(self, testElems)
        

""" class Scene(Scene):
    def construct(self):
        # create 10 Text onjects and add them to a VGroup
        #arr = VGroup(*[IntegerSortablBeMObject() for i in range(5)])
        arr = VGroup(
            Text("1.    for i = 0 to n-1 do"),
            Text("2.        min_idx = i"),
            Text("3.        for j = i+1 to n-1 do"),
            Text(" 4.            if (A[j] < A[min_idx])"),
            Text("5.            min_idx = j"),
            Text("6.            swap A[min_idx] with A[i]")
        ).scale(0.25).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT+UP)

        self.play(Write(arr)) 

     testElems[0].animate.move_to( UP) """
class Swap(Animation):
    def __init__(self, arr: SortSet, i, j, **kwargs):
        self.iLoc = arr[i].get_center()
        self.jLoc = arr[j].get_center()
        
        super().__init__(SortSet[i],)

    def interpolate_mobject(self, alpha):
        point = interpolate(self.start_point, self.end_point, alpha)
        self.mobject.move_to(point)

class SwapMobjectsAnimation(Animation):
    def __init__(self, scene, arr, i, j, **kwargs):
        self.scene = scene
        self.mobject1 = arr[i]
        self.mobject2 = arr[j]
        self.i = i
        self.j = j
        self.arr = arr
        super().__init__(arr[i], **kwargs)
        self.arr[self.i],self.arr[self.j] = self.arr[self.j],self.arr[self.i] 

    def interpolate_mobject(self, alpha):
        # Get the current positions and indices of the two mobjects
        pos1 = self.mobject1.get_center()
        pos2 = self.mobject2.get_center()

        # Calculate the new positions and indices of the two mobjects
        new_pos1 = interpolate(pos1, pos2, alpha)
        new_pos2 = interpolate(pos2, pos1, alpha)


        # Update the positions and indices of the two mobjects
        self.mobject1.move_to(new_pos1)
        self.mobject2.move_to(new_pos2)
        

        # Update the scene with the modified VGroup
        #self.scene.update_frame(self.scene.get_time())