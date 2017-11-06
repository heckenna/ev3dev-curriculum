
import time
import random
import ev3dev.ev3 as ev3
import robot_controller as robo
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()

    rc1 = ev3.RemoteControl(channel=1)
    rc2 = ev3.RemoteControl(channel=2)
    assert rc1.connected
    assert rc2.connected

main()