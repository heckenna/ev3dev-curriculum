#######################################################################################
#Project on Ev3                                                                       #
#   by Noah Heckenlively                                                              #
#######################################################################################



import mqtt_remote_method_calls as com

import ev3dev.ev3 as ev3
import time

import robot_controller as robo


class MyDelegate(object):

    def __init__(self):
        self.driving_list = [300, 100, "SIG1", False]
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
        self.running = True

    def change_turn_speed(self, new_turn_speed):
        self.driving_list[1] = new_turn_speed
        print("Turn speed set")

    def change_drive_speed(self, new_drive_speed):
        self.driving_list[0] = new_drive_speed
        print("Drive speed set")

    def determine_pixy_color(self, color):
        self.driving_list[2] = color
        ev3.Sound.speak("Color has been selected")
        print("Color has been selected.")

    def lettuce_go(self):
        #ev3.Sound.speak("Let us go then"''' you and I when the evening is spread out against the sky..."''').wait()
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        self.driving_list[3] = True

    def lettuce_stop(self):
        ev3.Sound.speak("Goodbye")
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
        self.running = False





def main():
    robot = robo.Snatch3r()
    my = MyDelegate()
    mqtt_client = com.MqttClient(my)
    mqtt_client.connect_to_pc()


    while True:
        #val = "String that will be sent from PC"
        robot.pixy.mode = my.driving_list[2]

        turn_speed = my.driving_list[1]
        drive_speed = my.driving_list[0]
        if my.driving_list[3]:
            #ev3.Sound.speak\
            print("Press the touch sensor to stop me.")
            while not robot.touch_sensor.is_pressed:
                x_coord = robot.pixy.value(1)
                y_coord = robot.pixy.value(2)
                width = robot.pixy.value(3)
                height = robot.pixy.value(4)

                print("x_coord is", x_coord)
                print("width is", width)

                if robot.ir_sensor.proximity < 5:
                    robot.drive_stop()
                    #print("Target found")
                    ev3.Sound.speak("I have located my target.")
                    break
                if width <= 1:
                    #ev3.Sound.speak("Color not found. Looking for the target")
                    print("Where art thou?")
                    robot.drive_forward(-my.driving_list[1], my.driving_list[1])
                    time.sleep(.5)
                elif 130 <= x_coord <= 210:
                    robot.drive_forward(my.driving_list[0], my.driving_list[0])
                elif x_coord < 130:
                    robot.drive_forward(-my.driving_list[1]/2, my.driving_list[1]/2)
                elif x_coord > 210:
                    robot.drive_forward(my.driving_list[1]/2, -my.driving_list[1]/2)


                if not my.running:
                    break
                time.sleep(0.1)

            robot.drive_stop()
            my.driving_list[3] = False



        #print("Would you like to search again?\nPress q to quit program.")

        if not my.running:
            break
        time.sleep(0.01)

    # All inside a big while loop inside of main


"""def change_turn_speed(self, new_turn_speed):
    my.driving_list[1] = new_turn_speed

def change_drive_speed(self, new_drive_speed):
    my.driving_list[0] = new_drive_speed

def determine_pixy_color(self, color):
    my.driving_list[2] = color
    my.Sound.speak("Color has been selcted")

def lettuce_go(self):
    ev3.Sound.speak("Let us go then you and I when the evening is spread out against the sky...").wait()
    my.driving_list[3] = True"""




main()