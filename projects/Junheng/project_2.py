
import time
import ev3dev.ev3 as ev3
import robot_controller as robo


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
            robot.turn_degrees(190, 100)
            speed = -1*speed
            robot.drive_forward(speed, speed)
            time.sleep(0.2)
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_RED:
            robot.drive_stop()
            robot.arm_up()
            robot.drive_forward(speed, speed)
            time.sleep(0.2)
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_WHITE:
            robot.drive_stop()
            robot.arm_down()
            robot.drive_forward(speed, speed)
            time.sleep(0.2)
        if robot.color_sensor.color == ev3.ColorSensor.COLOR_BLACK:
            robot.drive_stop()
            ev3.Sound.play("/home/robot/csse120/assets/sounds/awesome_pcm.wav").wait()
            robot.drive_forward(speed, speed)
            time.sleep(0.2)
        command = input("Press 'Q' to quit: ")
        if command == "q":
            robot.drive_stop()
            break
        time.sleep(0.1)


main()