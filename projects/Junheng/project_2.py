
import time
import random
import traceback
import ev3dev.ev3 as ev3
import robot_controller as robo
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


def main():
    robot = robo.Snatch3r()

    ev3.Sound.speak("Go along color blocks").wait()


main()