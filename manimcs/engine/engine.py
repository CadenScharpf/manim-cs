import os
import sys
import time
from manim import Scene, Circle, Square, config, LEFT, RIGHT
from ..algorithms import ArraySort
from ..renderer import ManimCSRenderer
from ..mobjs import SortableMobject, SVGMobject,  SortSet
from ..scene import ArraySortScene


#output_dir = "/app/output"


class ManimCsEngine:
    scene = None
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    commands = {
        "array": {
            "insertion-sort": ArraySort.insertion_sort,
            "bubble-sort": ArraySort.bubble_sort, 
            "selection-sort": ArraySort.selection_sort, 
            "merge-sort": ArraySort.unImplementedAlgorithm, 
            "quick-sort": ArraySort.unImplementedAlgorithm, 
            "heap-sort": ArraySort.unImplementedAlgorithm, 
            "radix-sort": ArraySort.unImplementedAlgorithm, 
            "counting-sort": ArraySort.unImplementedAlgorithm, 
            "bucket-sort": ArraySort.unImplementedAlgorithm},
        "tree" : {
            
        }
    }
    def __init__(self, command, *args, **kwargs):
        if command in self.commands.get("array"):
            if not 'inputValues' in kwargs:
                print("MANIM-CS-ERR: Please enter a list of integers to sort")
                raise ValueError("MANIM-CS-ERR: Please enter a list of integers to sort")
            if 'output_dir' in kwargs:
                self.output_dir = kwargs.get('output_dir')
            self.init_config(self.output_dir)


            elems = kwargs.get("inputValues")
            self.scene = ArraySortScene(self.commands.get("array").get(command), SortSet(elems))
        elif command in self.commands.get("tree"):
            print("MANIM-CS-INFO: Tree command")
        else:
            print("MANIM-CS-ERR: Command not recognized")
            raise ValueError("Command not recognized")
    def init_config(self, output_dir):
        if not os.path.exists(output_dir):
                os.makedirs(output_dir)

        config.media_width = "1920"
        config.frame_rate = 30
        config.output_file = output_dir +"/"+ time.strftime("%Y%m%d-%H%M%S")+".mp4"
        config.tex_dir = output_dir + "/tex"
        config.text_dir = output_dir + "/text"
        config.partial_movie_dir = output_dir + "/video/partial_movie_files"
    def generate(self):
        try:
            renderer = ManimCSRenderer(self.scene)
            renderer.render_scene()
            return config.output_file
        except Exception as e:
            print("MANIM-CS-ERR: Failed to generate animation")
            print(e)
            raise e


def getInputArray(offset):
    int_array = []
    if len(sys.argv) > offset+1:
        for arg in sys.argv[offset:]:
            int_array.append(int(arg))
    else:
        print("MANIM-CS-ERR: Please enter a list of integers to sort")
        raise ValueError("Input value must be an integer.")
    return int_array

""" if __name__ == "__main__":
    scene = None
    config.output_file = output_dir + "/video/"+time.strftime("%Y%m%d-%H%M%S")+".mp4"
    commands = {
        "array": {
            "insertion-sort": ArraySort.insertion_sort,
            "bubble-sort": ArraySort.bubble_sort, 
            "selection-sort": ArraySort.selection_sort, 
            "merge-sort": ArraySort.unImplementedAlgorithm, 
            "quick-sort": ArraySort.unImplementedAlgorithm, 
            "heap-sort": ArraySort.unImplementedAlgorithm, 
            "radix-sort": ArraySort.unImplementedAlgorithm, 
            "counting-sort": ArraySort.unImplementedAlgorithm, 
            "bucket-sort": ArraySort.unImplementedAlgorithm},
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
    renderer.render_scene() """