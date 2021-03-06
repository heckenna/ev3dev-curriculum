
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


class MyDelegate(object):
    def msg(self, message_from_ev3):
        print(message_from_ev3)


def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title('MQTT Remote')

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    speed_label = ttk.Label(main_frame, text='Speed:')
    speed_label.grid(row=0, column=0)
    speed_entry = ttk.Scale(main_frame, length=150, from_=100, to=850)
    speed_entry.grid(row=0, column=1, columnspan=2)

    forward_button = ttk.Button(main_frame, text='Forward')
    forward_button.grid(row=1, column=1)
    forward_button['command'] = lambda: send_forward(mqtt_client, speed_entry, speed_entry)
    root.bind('<Up>', lambda event: send_forward(mqtt_client, speed_entry, speed_entry))

    left_button = ttk.Button(main_frame, text='Left')
    left_button.grid(row=2, column=0)
    left_button['command'] = lambda: send_left(mqtt_client, speed_entry, speed_entry)
    root.bind('<Left>', lambda event: send_left(mqtt_client, speed_entry, speed_entry))

    stop_button = ttk.Button(main_frame, text='Stop')
    stop_button.grid(row=2, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<space>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(main_frame, text='Right')
    right_button.grid(row=2, column=2)
    right_button['command'] = lambda: send_right(mqtt_client, speed_entry, speed_entry)
    root.bind('<Right>', lambda event: send_right(mqtt_client, speed_entry, speed_entry))

    back_button = ttk.Button(main_frame, text='Back')
    back_button.grid(row=3, column=1)
    back_button['command'] = lambda: send_backward(mqtt_client, speed_entry, speed_entry)
    root.bind('<Down>', lambda event: send_backward(mqtt_client, speed_entry, speed_entry))

    up_button = ttk.Button(main_frame, text='Up')
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<a>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text='Down')
    down_button.grid(row=5, column=1)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<z>', lambda event: send_down(mqtt_client))

    e_button = ttk.Button(main_frame, text='Exit')
    e_button.grid(row=5, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))
    root.bind('<e>', lambda event: quit_program(mqtt_client, True))

    root.mainloop()


def send_up(mqtt_client):
    print('arm_up')
    mqtt_client.send_message('arm_up')


def send_down(mqtt_client):
    print('arm_down')
    mqtt_client.send_message('arm_down')


def send_forward(mqtt_client, left_speed_entry, right_speed_entry):
    print('go_forward')
    mqtt_client.send_message('drive_forward', [left_speed_entry.get(), right_speed_entry.get()])


def send_backward(mqtt_client, left_speed_entry, right_speed_entry):
    print('go_backward')
    mqtt_client.send_message('drive_backward', [left_speed_entry.get(), right_speed_entry.get()])


def send_left(mqtt_client, left_speed_entry, right_speed_entry):
    print('go_left')
    mqtt_client.send_message('drive_left', [left_speed_entry.get(), right_speed_entry.get()])


def send_right(mqtt_client, left_speed_entry, right_speed_entry):
    print('go_right')
    mqtt_client.send_message('drive_right', [left_speed_entry.get(), right_speed_entry.get()])


def send_stop(mqtt_client):
    print('stop')
    mqtt_client.send_message('drive_stop')


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print('shutdown')
        mqtt_client.send_message('shutdown')
    mqtt_client.close()
    exit()


main()
