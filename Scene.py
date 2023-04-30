import os
import sys
from manim import *
current_dir = os.path.dirname(os.path.abspath(__file__))
algorithms_dir = os.path.join(current_dir, '.', 'src/algorithms')
mob_dir = os.path.join(current_dir, '.', 'src/mobjects')
sys.path.append(algorithms_dir)
sys.path.append(mob_dir)
from src.mobjs.sort_set import SortSet
from src.mobjs.sortable_mobject import IntegerSortableMObject, SizeSortableMobject
from src.algorithms.sorting import Sorting
from sorting import Sorting
 
commands = {
    "array": ["insertion-sort", "bubble-sort", "selection-sort", "merge-sort", "quick-sort", "heap-sort", "radix-sort", "counting-sort", "bucket-sort"] ,
    "tree" : []
}

def getInputArray(index):
    int_array = []
    if len(sys.argv) > index+1:
        for arg in sys.argv[index:]:
            int_array.append(int(arg))
    else:
        print("MANIM-CS-ERR: Please enter a list of integers to sort")
        raise ValueError("Input value must be an integer.")
    return int_array

                  
class Scene(Scene):
    input = None
    def construct(self):
        # Create 10 squares and add them to a VGroup
        #arr = VGroup(*[IntegerSortableMObject() for i in range(5)])
        if(len(sys.argv) < 4):
            print("MANIM-CS-ERR: No command provided")
            raise ValueError("No command provided")

        if sys.argv[3] in commands.get("array"):
            elems = SortSet( getInputArray(4)).arrange(buff=0.5).center()
            self.add(elems)
            match sys.argv[3]:
                case "insertion-sort":
                    print("MANIM-CS-INFO: Insertion Sort")
                    Sorting.insertion_sort(self, elems)
                case "bubble-sort":
                    print("MANIM-CS-INFO: Bubble Sort")
                    Sorting.bubble_sort(self, elems)
                case "selection-sort":
                    print("MANIM-CS-INFO: Selection Sort")
                    Sorting.selection_sort(self, elems)
                case "merge-sort":
                    print("MANIM-CS-INFO: Merge Sort")
                case "quick-sort":
                    print("MANIM-CS-INFO: Quick Sort")
                case "heap-sort":
                    print("MANIM-CS-INFO: Heap Sort")
                case "radix-sort":
                    print("MANIM-CS-INFO: Radix Sort")
                case "counting-sort":
                    print("MANIM-CS-INFO: Counting Sort")
                case "bucket-sort":
                    print("MANIM-CS-INFO: Bucket Sort")
                case _:
                    print("MANIM-CS-ERR: Command not recognized")
                    raise ValueError("Command not recognized")

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