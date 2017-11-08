##############################################################################################
#Python 120 Project                                                                          #
#   by Noah Heckenlively                                                                     #
##############################################################################################



import tkinter
from tkinter import ttk
#from tkinter import fcntl
import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3

import time
import random

class MyDelegate(object):

    def __init__(self):
        self.running = True


def main():
    root = tkinter.Tk()
    root.title('Color Selection for the ball.')

    main_frame = ttk.Frame(root, padding=40, relief='raised')
    main_frame.grid()

    color1_button = ttk.Button(main_frame, text="Red(?)")
    color1_button.grid(row=1, column=0)
    color1_button['command'] = lambda: print('Hello')

    color2_button = ttk.Button(main_frame, text="Yellow(?)")
    color2_button.grid(row=1, column=1)
    color2_button['command'] = lambda: print('Goodbye')

    color3_button = ttk.Button(main_frame, text="Green(?)")
    color3_button.grid(row=1, column=2)
    color3_button['command'] = lambda: print('Bonjour!')

    color4_button = ttk.Button(main_frame, text="Brown(?)")
    color4_button.grid(row=1, column=3)
    color4_button['command'] = lambda: print('Au Revoir')

    color5_button = ttk.Button(main_frame, text="Scarlet(?)")
    color5_button.grid(row=1, column=4)
    color5_button['command'] = lambda: print('Salut')

    exit_button = ttk.Button(main_frame, text="Exit")
    exit_button.grid(row=3, column=4)
    exit_button['command'] = lambda: print('So long dudes')


    root.mainloop()




main()