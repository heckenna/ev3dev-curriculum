"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time

class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""
    
    # DONE: Implement the Snatch3r class as needed when working the sandbox exercises
    # (and delete these comments)
    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor()
        self.rc1 = ev3.RemoteControl(channel=1)
        self.rc2 = ev3.RemoteControl(channel=2)
        self.rc3 = ev3.RemoteControl(channel=3)
        self.rc4 = ev3.RemoteControl(channel=4)
        self.color_sensor = ev3.ColorSensor()
        self.ir_sensor = ev3.InfraredSensor()
        self.pixy = ev3.Sensor(driver_name="pixt-lego")

        assert ev3.ColorSensor()
        assert ev3.InfraredSensor()
        assert ev3.Sensor(driver_name="pixt-lego")


    def seek_beacon(self):
        assert self.ir_sensor
        beacon_seeker = ev3.BeaconSeeker(channel=1)
        while True:
            current_heading = self.ir_sensor.beacon_seeker.heading
            current_distance = self.ir_sensor.beacon_seeker.distance
            if current_distance == -128:
                print("IR Remote not found. Distance is -128")
                self.drive_stop()
            else:
                if math.fabs(current_heading) < 2:
                    print("On the right heading. Distance: ", current_distance)
                    if current_distance == 0:
                        self.drive_stop()
                        print("Beacon found!")
                        return True
                    self.drive_forward(300, 300)
                elif math.fabs(current_heading) >= 10:
                    self.drive_stop()
                    print("Heading is too far off to fix: ", current_heading)
                else:
                    print("Adjusting heading: ", current_heading)
                    if current_heading < 0:
                        self.drive_forward(-100, 100)
                    else:
                        self.drive_forward(100, -100)
            time.sleep(0.1)

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.01)

    def shutdown(self):
        self.running = False

    def drive_inches(self, inches_target, speed_deg_per_second):
        # Check that the motors are actually connected
        assert self.left_motor.connected
        assert self.right_motor.connected

        self.right_motor.run_to_rel_pos(position_sp = inches_target * 90, speed_sp = speed_deg_per_second)
        self.left_motor.run_to_rel_pos(position_sp = inches_target * 90, speed_sp = speed_deg_per_second)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        # Check that the motors are actually connected
        assert self.left_motor.connected
        assert self.right_motor.connected

        self.right_motor.run_to_rel_pos(position_sp = degrees_to_turn * 5, speed_sp = turn_speed_sp)
        self.left_motor.run_to_rel_pos(position_sp = degrees_to_turn * -5, speed_sp = turn_speed_sp)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def arm_calibration(self):
        assert self.arm_motor.connected
        assert self.touch_sensor

        self.arm_motor.run_forever(speed_sp=900)

        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        ev3.Sound.beep()

        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(position_sp=-arm_revolutions_for_full_range)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep()

        self.arm_motor.position = 0

    def arm_up(self):
        assert self.arm_motor.connected
        assert self.touch_sensor

        self.arm_motor.run_to_rel_pos(position_sp=14.2 * 360, speed_sp=900)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action='brake')
        ev3.Sound.beep()

    def arm_down(self):
        assert self.arm_motor.connected
        assert self.touch_sensor

        self.arm_motor.run_to_abs_pos(position_sp=0)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep()

    def drive_forward(self, left_sp, right_sp):
        assert self.left_motor.connected
        assert self.right_motor.connected

        left_sp = int(left_sp)
        right_sp = int(right_sp)

        self.right_motor.run_forever(speed_sp = right_sp)
        self.left_motor.run_forever(speed_sp = left_sp)

    def drive_left(self, left_sp, right_sp):
        assert self.left_motor.connected
        assert self.right_motor.connected

        left_sp = int(left_sp)
        right_sp = int(right_sp)

        self.right_motor.run_forever(speed_sp = right_sp)
        self.left_motor.run_forever(speed_sp = -left_sp)

    def drive_right(self, left_sp, right_sp):
        assert self.left_motor.connected
        assert self.right_motor.connected

        left_sp = int(left_sp)
        right_sp = int(right_sp)

        self.right_motor.run_forever(speed_sp  =-right_sp)
        self.left_motor.run_forever(speed_sp = left_sp)

    def drive_backward(self, left_sp, right_sp):
        assert self.left_motor.connected
        assert self.right_motor.connected

        left_sp = int(left_sp)
        right_sp = int(right_sp)

        self.right_motor.run_forever(speed_sp = -right_sp)
        self.left_motor.run_forever(speed_sp = -left_sp)

    def drive_stop(self):
        assert self.left_motor.connected
        assert self.right_motor.connected

        self.right_motor.stop(stop_action = 'brake')
        self.left_motor.stop(stop_action = 'brake')


    def left_motor_forward(self):
        assert  self.left_motor.connected
        self.left_motor.run_forever(speed_sp=600)
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)

    def left_motor_backward(self):
        assert  self.left_motor.connected
        self.left_motor.run_forever(speed_sp=-600)
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)

    def right_motor_forward(self):
        assert  self.right_motor.connected
        self.right_motor.run_forever(speed_sp=600)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

    def right_motor_backward(self):
        assert  self.right_motor.connected
        self.right_motor.run_forever(speed_sp=-600)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
