
import time
import random
import ev3dev.ev3 as ev3
import robot_controller as robo
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk

def test():
    robot = robo.Snatch3r()
    left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
