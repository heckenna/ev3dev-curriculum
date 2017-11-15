
import time
import ev3dev.ev3 as ev3
import robot_controller as robo
import mqtt_remote_method_calls as com


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    touch_sensor = ev3.TouchSensor()
    assert touch_sensor

    ev3.Sound.speak('Guide me back home').wait()
    while True:
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_BLUE:
            robot.drive_stop()
            robot.turn_degrees(380, 300)
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_RED:
            robot.drive_stop()
            ev3.Sound.speak('you just killed me')
            robot.arm_down()
            exit()
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_YELLOW:
            robot.drive_stop()
            ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav")
        while not touch_sensor.is_pressed:
            time.sleep(5)
            ev3.Sound.speak('I am home')
            time.sleep(1)
            ev3.Sound.speak('Here is the bone')
            exit()

    robot.loop_forever()

#     rc1 = ev3.RemoteControl(channel=1)
#     rc2 = ev3.RemoteControl(channel=2)
#     assert rc1.connected
#     assert rc2.connected
#
#     rc1.on_red_up = lambda state: left_motor_forward_button(state, robot)
#     rc1.on_red_down = lambda state: left_motor_backward_button(state, robot)
#     rc1.on_blue_up = lambda state: right_motor_forward_button(state, robot)
#     rc1.on_blue_down = lambda state: right_motor_backward_button(state, robot)
#
#     rc2.on_red_up = lambda state: handle_arm_up_button(state, robot)
#     rc2.on_red_down = lambda state: handle_arm_down_button(state, robot)
#     rc2.on_blue_up = lambda state: handle_calibrate_button(state, robot)
#     rc2.on_blue_down = lambda state: handle_calibrate_button(state, robot)
#
#     while True:
#         rc1.process()
#         rc2.process()
#         time.sleep(0.1)
#
#
# def left_motor_forward_button(button_state, robot):
#     if button_state:
#         robot.left_motor_forward()
#     else:
#         robot.left_motor.stop()
#
# def left_motor_backward_button(button_state, robot):
#     if button_state:
#         robot.left_motor_backward()
#     else:
#         robot.left_motor.stop()
#
# def right_motor_forward_button(button_state, robot):
#     if button_state:
#         robot.right_motor_forward()
#     else:
#         robot.right_motor.stop()
#
# def right_motor_backward_button(button_state, robot):
#     if button_state:
#         robot.right_motor_backward()
#     else:
#         robot.right_motor.stop()
#
# def handle_arm_up_button(button_state, robot):
#     if button_state:
#         robot.arm_up()
#
# def handle_arm_down_button(button_state, robot):
#     if button_state:
#         robot.arm_down()
#
# def handle_calibrate_button(button_state, robot):
#     if button_state:
#         robot.arm_calibration()
