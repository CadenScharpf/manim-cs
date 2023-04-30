import sys
from manim import Scene, Circle, Square, config, LEFT, RIGHT
from algorithms import Sorting
from mobjs import SortableMobject, SVGMobject,  SortSet

class ArraySortScene(Scene):
    def __init__(self, algorithm,elems: SortSet):
        super().__init__()
        self.algorithm = algorithm
        self.elems = elems

    def construct(self):
        self.add(self.elems)
        self.algorithm(self,self.elems)

class ManimCSRenderer:
    def __init__(self, scene: Scene):
        self.scene = scene

    def render_scene(self):
        # Configure rendering settings
        config.media_width = "1920"
        config.media_height = "1080"
        config.frame_rate = 30
        # Render the scene
        self.scene.render()

def unImplementedAlgorithm(scene: Scene, elems: SortSet):
    print("MANIM-CS-ERR: Algorithm not implemented")
    raise NotImplementedError("Algorithm not implemented")

def getInputArray(offset):
    int_array = []
    if len(sys.argv) > offset+1:
        for arg in sys.argv[offset:]:
            int_array.append(int(arg))
    else:
        print("MANIM-CS-ERR: Please enter a list of integers to sort")
        raise ValueError("Input value must be an integer.")
    return int_array


if __name__ == "__main__":
    scene = None
    commands = {
        "array": {
            "insertion-sort": Sorting.insertion_sort,
            "bubble-sort": Sorting.bubble_sort, 
            "selection-sort": Sorting.selection_sort, 
            "merge-sort": unImplementedAlgorithm, 
            "quick-sort": unImplementedAlgorithm, 
            "heap-sort": unImplementedAlgorithm, 
            "radix-sort": unImplementedAlgorithm, 
            "counting-sort": unImplementedAlgorithm, 
            "bucket-sort": unImplementedAlgorithm},
        "tree" : {
            
        }
    }

    if(len(sys.argv) < 1):
        print("MANIM-CS-ERR: No command provided")
        raise ValueError("No command provided")

    command = sys.argv[1]
    if command in commands.get("array"):
        scene = ArraySortScene(commands.get("array").get(command), SortSet(getInputArray(2)))
    elif sys.argv[1] in commands.get("tree"):
        print("MANIM-CS-INFO: Tree command")
    else:
        print("MANIM-CS-ERR: Command not recognized")
        raise ValueError("Command not recognized")
    
    # Create a renderer object and pass the scene object to it
    renderer = ManimCSRenderer(scene)

    # Call the render_scene method to render the scene
    renderer.render_scene()