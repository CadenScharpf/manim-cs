import os
from manimcs import ManimCsEngine

engine = ManimCsEngine("selection-sort", inputValues=[1, 0])
""" , output_dir=os.path.join(os.path.dirname(__file__), 'outputTest2') """
engine.generate()