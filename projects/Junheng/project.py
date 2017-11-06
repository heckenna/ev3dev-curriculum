
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

    ev3.Sound.speak("Beacon pickup").wait()
    try:
        while True:
            found_beacon = robot.seek_beacon()
            if found_beacon:
                ev3.Sound.speak("I got the beacon")
                robot.arm_up()
                time.sleep(1)
                robot.arm_down()
            command = input("Press 'N' to continue: ")
            if command == "n":
                print("Beacon picked up")
                break
    except:
        traceback.print_exc()
        ev3.Sound.speak("Error")


main()