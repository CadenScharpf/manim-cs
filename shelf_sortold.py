from big_ol_pile_of_manim_imports import *
import os
import pyclbr



class SelectionSort(Scene):

    CONFIG = {
        "initial_color" : "#5CD0B3",
        "i_color" : "#ffcc00",
        "j_color" : WHITE,
        "min_idx_color" : "#3b8774",

        "FIRST_ELEM_LOCATION" : -6,
        "loops" : 0,
        "swaptime" : .5,
        "runtime" : .5,
    }

    def construct(self):

        # Colors #
        initial_color = "#5CD0B3"
        i_color =  "#ffcc00"
        j_color = WHITE
        min_idx_color = "#3b8774"

        # Data #
        FIRST_ELEM_LOCATION = -6
        loops = 0
        swaptime = .5
        runtime = .5

        # MOBJECTS #
        shelf = Line(np.array([-6.8,-2,0]),np.array([6.8,-2,0]))

        i_text = SingleStringTexMobject("i = " + str(0))
        i_text_location = (DOWN*3+LEFT*3)

        j_text = SingleStringTexMobject("j = " + str(0))
        j_text_location = (DOWN*3+RIGHT*3)

        loops_text = SingleStringTexMobject("loops = " + str(loops))
        loops_text_location = (UP*3 + LEFT*5)

        elements = list(map(SingleStringTexMobject, [
            "4", "1", "9", "7", "2", "3", "6", "8", "0"
        ]))


        # Position/Color MOBJECTS #
        i_text.move_to(i_text_location)
        j_text.move_to(j_text_location)
        loops_text.move_to(loops_text_location)

        for elem in reversed(elements):
            print(elem.tex_string)
            elem.add_background_rectangle(color=initial_color)
            elem.move_to(DOWN+LEFT*FIRST_ELEM_LOCATION)
            FIRST_ELEM_LOCATION = FIRST_ELEM_LOCATION+1.5


        # Display Elements
        self.play(*list(map(FadeIn, elements)))
        self.play(
            FadeIn(shelf),
            FadeIn(i_text),
            FadeIn(j_text),
            FadeIn(loops_text)
        )

    
        # Sorting Loop #
        i = 0
        while i < 8:

            update_i = SingleStringTexMobject("i = " + str(i))
            update_i.move_to(i_text_location)

            update_j = SingleStringTexMobject("j = " + str(i+1))
            update_j.move_to(j_text_location)

            self.play(
                MyFadeToColor(elements[i], i_color),
                Transform(j_text,update_j),
                Transform(i_text,update_i),
                run_time = runtime
            )
            self.wait(2)

            min_idx = i
            j = i+1
            
            while j < 9:
                loops = loops + 1
                update_loops = SingleStringTexMobject("loops = " + str(loops))
                update_loops.move_to(loops_text_location)

                update_j = SingleStringTexMobject("j = " + str(j))
                update_j.move_to(j_text_location)
                
                self.play(
                    Transform(j_text,update_j),
                    Transform(loops_text,update_loops),
                    MyFadeToColor(elements[j], j_color),
                    run_time = runtime
                )

                if int(elements[j].tex_string) < int(elements[min_idx].tex_string) and min_idx == i:
                    self.play(
                        MyFadeToColor(elements[j],
                        min_idx_color,
                        run_time = runtime)
                    )
                    min_idx = j
                elif int(elements[j].tex_string) < int(elements[min_idx].tex_string):
                    self.play(
                        MyFadeToColor(elements[min_idx], initial_color),
                        MyFadeToColor(elements[j], min_idx_color),
                        run_time = runtime
                    )
                    min_idx = j
                else:
                    self.play(MyFadeToColor(elements[j], initial_color, run_time = runtime))
                
                j = j+1

            # Swap if i != min_idx
            if min_idx != i:
                self.wait(1)
                self.play(
                    ApplyMethod(elements[i].move_to,LEFT+UP),
                    ApplyMethod(elements[min_idx].move_to,RIGHT+UP),
                    run_time = swaptime
                )
                self.play(
                    ApplyMethod(elements[i].move_to,DOWN+(LEFT*6)+RIGHT*1.5*min_idx),
                    ApplyMethod(elements[min_idx].move_to,DOWN+(LEFT*6)+RIGHT*1.5*i),
                    run_time = swaptime
                )
                # Swap #
                temp = elements[i]
                elements[i] = elements[min_idx]
                elements[min_idx] = temp
                self.wait(1)
                
            self.play(
                MyFadeToColor(elements[min_idx], initial_color),
                MyFadeToColor(elements[i], initial_color),
                run_time = runtime
            )
            i = i+1








if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'shelf_sort'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("shelf_sort.py %s -l" % item.name)  #Does not play files