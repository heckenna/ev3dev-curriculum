
import traceback
import ev3dev.ev3 as ev3
import robot_controller as robo
import project_ev3 as p3


def main():
    robot = robo.Snatch3r()
    ev3.Sound.speak("I will get the bone").wait()
    try:
        while True:
            found_beacon = robot.seek_beacon()
            if found_beacon:
                robot.arm_up()
                print("Beacon picked up")
                ev3.Sound.speak("I got the bone")
            command = input("Press 'N' to continue: ")
            if command == "n":
                break
    except:
        traceback.print_exc()
        ev3.Sound.speak("Error")
        exit()


main()
p3.main()
