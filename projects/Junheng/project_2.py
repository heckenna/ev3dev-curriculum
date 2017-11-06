
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
    speed = 300

    ev3.Sound.speak("Go along color blocks").wait()
    while True:
        robot.drive_forward(speed, speed)
        if robot.ir_sensor.proximity <= 2:
            robot.drive_stop()
            print('Running into a object')
            break
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_BLUE:
            robot.drive_stop()
            robot.turn_degrees(180, 100)
            speed = -1*speed
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_RED:
            robot.drive_stop()
            robot.arm_calibration()
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_BLACK:
            robot.drive_stop()
            ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav").wait()
        time.sleep(0.1)


main()