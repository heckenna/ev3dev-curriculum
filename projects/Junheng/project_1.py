
import traceback
import ev3dev.ev3 as ev3
import robot_controller as robo


def main():
    robot = robo.Snatch3r()

    ev3.Sound.speak("Beacon pickup").wait()
    try:
        while True:
            found_beacon = robot.seek_beacon()
            if found_beacon:
                print("Beacon picked up")
                ev3.Sound.speak("I got the beacon")
                robot.arm_up()
            command = input("Press 'N' to continue: ")
            if command == "n":
                break
    except:
        traceback.print_exc()
        ev3.Sound.speak("Error")
        exit()


main()