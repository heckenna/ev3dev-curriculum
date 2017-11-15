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

class MyDelegateOnThePc(object):

    def __init__(self):
        self.running = True


def main():
    root = tkinter.Tk()
    root.title('Color Selection for the ball')

    pc_delegate = MyDelegateOnThePc()
    mqtt_client = com.MqttClient(pc_delegate)
    mqtt_client.connect_to_ev3()

    list = ['SIG1', 'SIG2', 'SIG3', 'SIG4', 'SIG5']

    print("Please select a color or select a random one.")

    main_frame = ttk.Frame(root, padding = 40 , relief='raised')
    main_frame.grid()

    color1_button = ttk.Button(main_frame, text="Green")
    color1_button.grid(row=1, column=0)
    color1_button['command'] = lambda: mqtt_client.send_message("determine_pixy_color", ["SIG1"])

    color2_button = ttk.Button(main_frame, text="Purple")
    color2_button.grid(row=1, column=1)
    color2_button['command'] = lambda: mqtt_client.send_message("determine_pixy_color", ["SIG2"])

    color3_button = ttk.Button(main_frame, text="Blue")
    color3_button.grid(row=1, column=2)
    color3_button['command'] = lambda: mqtt_client.send_message("determine_pixy_color", ["SIG3"])

    """color4_button = ttk.Button(main_frame, text="Blue")
    color4_button.grid(row=1, column=3)
    color4_button['command'] = lambda: mqtt_client.send_message("determine_pixy_color", ["SIG4"])"""

    '''color5_button = ttk.Button(main_frame, text="Scarlet(?)")
    color5_button.grid(row=1, column=4)
    color5_button['command'] = lambda: mqtt_client.send_message("determine_pixy_color", ["SIG5"])'''

    rand_button = ttk.Button(main_frame, text="Random")
    rand_button.grid(row=2, column=2)
    rand_button['command'] = lambda: mqtt_client.send_message("determine_pixy_color", [list[random.randrange(0,2)]])

    drive_entry = ttk.Entry(main_frame, width=11)
    drive_entry.grid(row=3, column=0)

    drive_button = ttk.Button(main_frame, text="Drive Speed")
    drive_button.grid(row=3, column=1)
    drive_button['command'] = lambda: message_to_robot(mqtt_client, "change_drive_speed", drive_entry)

    turn_entry = ttk.Entry(main_frame, width = 11)
    turn_entry.grid(row=4, column=0)

    turn_button = ttk.Button(main_frame, text="Turn Speed")
    turn_button.grid(row=4, column=1)
    turn_button['command'] = lambda: message_to_robot(mqtt_client, "change_turn_speed", turn_entry)

    start_button = ttk.Button(main_frame, text="Start")
    start_button.grid(row=3, column=4)
    start_button['command'] = lambda: mqtt_client.send_message("lettuce_go")

    exit_button = ttk.Button(main_frame, text="Exit")
    exit_button.grid(row=4, column=4)
    exit_button['command'] = lambda: stop_right_there(mqtt_client)


    root.mainloop()


def message_to_robot(mqtt_client, message_name, entry_box):
    #print("wnet to function")
    msg = int(entry_box.get())
    mqtt_client.send_message(message_name, [msg])

def stop_right_there(mqtt_client):
    mqtt_client.send_message("lettuce_stop")


main()

