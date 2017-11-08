#######################################################################################
#Project on Ev3                                                                       #
#   by Noah Heckenlively                                                              #
#######################################################################################


import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


class MyDelegate(object):

    def __init__(self):
        self.driving_list = [300, 100, "SIG1", False]

    def change_turn_speed(self, new_turn_speed):
        self.driving_list[1] = new_turn_speed

    def change_drive_speed(self, new_drive_speed):
        self.driving_list[0] = new_drive_speed

    def determine_pixy_color(self, color):
        self.driving_list[2] = color

def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)

    val = "String that will be sent from PC"
    robot.pixy.mode = MyDelegate.driving_list[2]

    turn_speed = MyDelegate.driving_list[1]
    drive_speed = MyDelegate.driving_list[0]
    if MyDelegate.driving_list[4]:
        ev3.Sound.speak("Press the touch sensor to stop me.")
        while not robot.touch_sensor.is_pressed:
            x_coord = robot.pixy.value(1)
            y_coord = robot.pixy.value(2)
            width = robot.pixy.value(3)
            height = robot.pixy.value(4)

            if robot.ir_sensor.proximity < 2:
                robot.drive_stop()
                ev3.Sound.speak("I have located my target.")
                MyDelegate.driving_list[4] = False
                break
            if x_coord < 150:
                robot.drive_forward(-turn_speed, turn_speed)
            elif x_coord > 170:
                robot.drive_forward(turn_speed, -turn_speed)
            elif 150 <= x_coord <= x_coord:
                robot.drive_forward(drive_speed, drive_speed)
            if width <= 1:
                ev3.Sound.speak("Color not found. Looking for the ball")
                robot.drive_forward(-turn_speed/2, turn_speed/2)


            time.sleep(0.1)



    print("Would you like to search again?\nPress q to quit program.")

    time.sleep(0.01)
    # All inside a big while loop inside of main







main()