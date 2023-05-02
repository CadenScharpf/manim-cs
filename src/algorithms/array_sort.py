import os
import sys

from matplotlib.sankey import UP
import numpy as np

from ..mobjs.sort_set import SortSet



""" 
current_dir = os.path.dirname(os.path.abspath(__file__))
mobs_dir = os.path.join(current_dir, '..', 'mobjects')
sys.path.append(mobs_dir)
from src.mobjs.sort_set import SortSet """

from manim import FadeIn, FadeOut, Animation, VGroup, Square, Mobject, Tex, Scene, ApplyMethod, YELLOW, GREEN, GREY, Text, DOWN, LEFT, UP, interpolate, Write, WHITE, Arrow, RIGHT, RED, Line

class ArraySort:

    @staticmethod
    def selection_sort(scene: Scene, mObjArr: SortSet):
        defaultColor = mObjArr[0].get_color()
        mIdxColor = YELLOW
        jColor = WHITE

        dCodeBlockColor = WHITE

        codeBlock = VGroup(
            Text("1.    for i = 0 to n-1 do"),
            Text("2.        minIdx = i"),
            Text("3.        for j = i+1 to n-1 do"),
            Text("4.            if (A[j] < A[minIdx])"),
            Text("5.                minIdx = j"),
            Text("6.        swap A[minIdx] with A[i]")
        ).set_color(dCodeBlockColor).scale(0.4).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(LEFT+UP)
        linePtr = Arrow (codeBlock[0].get_right() + RIGHT, codeBlock[0], color=GREEN).move_to(codeBlock[0].get_right() + RIGHT*.5)
        
        iLbl = Text("[i]")
        iArrow = Arrow( iLbl, iLbl.get_top() + UP, color=WHITE)
        iGroup = VGroup(iLbl, iArrow).move_to(mObjArr[0].get_bottom() + DOWN)



        scene.play(Write(codeBlock))
        scene.wait(2)

        scene.play(FadeIn(linePtr))
        scene.wait(0.7)
        for i in range(len(mObjArr)):

            jLbl = Text("[j]")
            jArrow = Arrow( jLbl, jLbl.get_top() + UP, color=WHITE)
            jGroup = None# VGroup(jLbl, jArrow).move_to(mObjArr[1].get_bottom() + DOWN) if j < (len(mObjArr)-1) else None
            if(i == 0): scene.play(FadeIn(iGroup))

            scene.play(iGroup.animate.move_to(mObjArr[i].get_bottom() + DOWN))
            scene.wait(0.7) 

            scene.play(ApplyMethod(mObjArr[i].set_color,mIdxColor),linePtr.animate.move_to(codeBlock[1].get_right() + RIGHT*.5))
            scene.wait(0.7)
            min_idx = i

            scene.play(linePtr.animate.move_to(codeBlock[2].get_right() + RIGHT*.5))
            scene.wait(0.7)
            for j in range(i + 1, len(mObjArr)):
                if(j <= (len(mObjArr)-1)):
                    if(j == i+1): 
                        jGroup = VGroup(jLbl, jArrow).move_to(mObjArr[j].get_bottom() + DOWN)
                        scene.play(FadeIn(jGroup), ApplyMethod(mObjArr[j].set_color, jColor),linePtr.animate.move_to(codeBlock[3].get_right() + RIGHT*.5))
                    else: 
                        scene.play(jGroup.animate.move_to(mObjArr[j].get_bottom() + DOWN), ApplyMethod(mObjArr[j].set_color, jColor),linePtr.animate.move_to(codeBlock[3].get_right() + RIGHT*.5))
                

                
                scene.play(linePtr.animate.move_to(codeBlock[3].get_right() + RIGHT*.5))
                
                if mObjArr[j] < mObjArr[min_idx]:
                    scene.play(ApplyMethod(mObjArr[min_idx].set_color, defaultColor), ApplyMethod(mObjArr[j].set_color, mIdxColor), linePtr.animate.move_to(codeBlock[4].get_right() + RIGHT*.5))
                    scene.wait(0.7)
                    min_idx = j
                else:
                    scene.play(ApplyMethod(mObjArr[j].set_color, defaultColor))

            scene.play(linePtr.animate.move_to(codeBlock[5].get_right() + RIGHT*.5))

            swap_indices(scene, mObjArr, i, min_idx, useBuffer=True)

            scene.play(ApplyMethod(mObjArr[i].set_color, GREEN), FadeOut(jGroup))
        scene.play(FadeOut(linePtr), FadeOut(iGroup), FadeOut(codeBlock))
        return mObjArr

    @staticmethod
    def bubble_sort(scene: Scene, mObjArr: SortSet):

        dCodeBlockColor = WHITE

        codeBlock = VGroup(
            Text("1.    for i = 0 to n-1 do"),
            Text("2.        for j = 0 to n-i-1 do"),
            Text("3.            if (A[j] > A[j+1])"),
            Text("4.                swap A[j] with A[j+1]")
        ).set_color(dCodeBlockColor).scale(0.4).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(LEFT+UP)
        linePtr = Arrow (codeBlock[0].get_right() + RIGHT, codeBlock[0], color=GREEN).move_to(codeBlock[0].get_right() + RIGHT*.5)

        iLbl = Text("[i]")
        iArrow = Arrow( iLbl, iLbl.get_top() + UP, color=WHITE)
        iGroup = VGroup(iLbl, iArrow).move_to(mObjArr[0].get_bottom() + DOWN)

        scene.play(Write(codeBlock))
        scene.wait(2)

        scene.play(FadeIn(linePtr))
        scene.wait(0.7)
        for i in range(len(mObjArr)):
            jLbl = Text("[j]")
            jArrow = Arrow( jLbl, jLbl.get_top() + UP, color=WHITE)
            jGroup = None
            if(i == 0): scene.play(FadeIn(iGroup))

            scene.play(iGroup.animate.move_to(mObjArr[len(mObjArr) - i-1].get_bottom() + DOWN))
            scene.wait(0.7)

            scene.play(linePtr.animate.move_to(codeBlock[1].get_right() + RIGHT*.5))
            scene.wait(0.7)
            for j in range(0, len(mObjArr)-i-1):
                if(j <= (len(mObjArr)-1)):
                    if(j == 0): 
                        jGroup = VGroup(jLbl, jArrow).move_to(mObjArr[j].get_bottom() + DOWN)
                        scene.play(FadeIn(jGroup), linePtr.animate.move_to(codeBlock[2].get_right() + RIGHT*.5))
                    else: 
                        scene.play(jGroup.animate.move_to(mObjArr[j].get_bottom() + DOWN),linePtr.animate.move_to(codeBlock[2].get_right() + RIGHT*.5))
                

                
                scene.play(linePtr.animate.move_to(codeBlock[2].get_right() + RIGHT*.5))
                
                if mObjArr[j] > mObjArr[j+1]:
                    scene.wait(0.7)
                    scene.play(linePtr.animate.move_to(codeBlock[3].get_right() + RIGHT*.5))
                    swap_indices(scene, mObjArr, j, j+1, useBuffer=False)


            #scene.play(linePtr.animate.move_to(codeBlock[4].get_right() + RIGHT*.5))

            scene.play(ApplyMethod(mObjArr[len(mObjArr)-i-1].set_color, GREEN), FadeOut(jGroup))
        ApplyMethod(mObjArr[0].set_color, GREEN)
        scene.play(FadeOut(linePtr), FadeOut(iGroup), FadeOut(codeBlock))
        return mObjArr

    @staticmethod
    def insertion_sort(scene: Scene, mObjArr: SortSet):
            centers = [elem.get_center() for elem in mObjArr.submobjects]
            for i in range(1, len(mObjArr)):

                key = mObjArr[i]

                if(mObjArr[i-1] > key):
                    keyCopy = key.copy().move_to(key.get_center() + UP*2)

                    scene.play(FadeIn(keyCopy))

                    j = i-1
                    while j >= 0 and mObjArr[j] > key:
                        shift_index(scene, mObjArr, j, centers, direction="right")
                        # swap_indices(scene, mObjArr, j, j+1, useBuffer=False)
                        j = j-1
                    
                    mObjArr[j+1] = keyCopy
                    scene.play(ApplyMethod(keyCopy.move_to, centers[j+1]))

            return mObjArr
    
    @staticmethod
    def unImplementedAlgorithm(scene: Scene, elems: SortSet):
        print("MANIM-CS-ERR: Algorithm not implemented")
        raise NotImplementedError("Algorithm not implemented")
    
    

def swap_indices(scene, arr, i, j, useBuffer=False):
        if i == j: return
        arr[i], arr[j] = arr[j], arr[i]
        if useBuffer: buffer_swap(scene, arr[i], arr[j]) 
        else: direct_swap(scene, arr[i], arr[j])

def get_divider_line_coordinates(scene, arr, i, j):
    midpoint = None
    if((i<0 | j<=i) and j < len(arr)):
        midpoint = arr[j].get_center()
    else:
        midpoint = (arr[i].get_center() + arr[j].get_center())/2
    return np.array([midpoint+UP, midpoint+DOWN, 0])
        

def shift_index(scene, arr, i, centers, direction="left"):
    offset = -1 if direction == "left" else 1
    shift_pos = arr[i+offset].get_center()
    arr[i+offset] = arr[i]
    FadeOut(arr[i])
    scene.play(ApplyMethod(arr[i].move_to, centers[i+offset]))


# direct swap: 
# Directly swap positions and indices i,j in the arr vgroup, without using a buffer
def direct_swap(scene: Scene,iObj: VGroup, jObj:  VGroup):
    scene.play(iObj.animate.move_to(jObj.get_center()), jObj.animate.move_to(iObj.get_center()))

# buffer swap:
# Swap positions and indices i,j in the arr vgroup, using a buffer
def buffer_swap(scene: Scene,iObj: VGroup, jObj: VGroup):
    copy = iObj.copy()
    copy.move_to(iObj.get_center())
    #circle_copy.shift(UP)
    scene.add(copy)
    scene.play(iObj.animate.move_to(UP*2))
    scene.wait(.5)
    jPos = jObj.get_center()
    scene.play(jObj.animate.move_to(copy.get_center()), iObj.animate.move_to(jPos),  FadeOut(copy))
    scene.remove(copy) 