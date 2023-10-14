#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, InfraredSensor, GyroSensor, UltrasonicSensor)
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

import random

#------------------------------------------------------------------------------
# initialization

distance_sensor = UltrasonicSensor(Port.S1)
gyro_sensor     = GyroSensor(Port.S2)
bumper          = TouchSensor(Port.S3)
obstacle_sensor = InfraredSensor(Port.S4)

robot = DriveBase(left_motor = Motor(Port.B), right_motor = Motor(Port.C), wheel_diameter = 62.4, axle_track = 109.605 )     # mm
robot.settings(straight_speed = 100, straight_acceleration = 100, turn_rate = 100, turn_acceleration = 100)

data  = DataLog('time / s', 'distance / m', 'angle motors / °', 'angle gyro / °', name='path', timestamp=False)
watch = StopWatch()

#------------------------------------------------------------------------------
# calibration

# data  = DataLog('time / s', 'distance driven motor / mm', 'distance ultrasonic / mm', 'distance infrared / %', name='distance_sensor', timestamp=False)
# robot.drive(speed = 100, turn_rate = 0)
# for n in range(300):
#     data.log(watch.time()/1000, robot.distance(), distance_sensor.distance(), obstacle_sensor.distance())
#     wait(100)
# robot.stop()


gyro_sensor.reset_angle(0)
robot.turn(3*360)  # °
wait(100)
factor = gyro_sensor.angle() / (3*360)

robot.reset()
gyro_sensor.reset_angle(0)

#------------------------------------------------------------------------------
# main loop

data.log(watch.time()/1000, robot.distance()/1000, robot.angle(), gyro_sensor.angle()/factor)


# for n in range(10):
#     robot.turn(360)
#     data.log(watch.time()/1000, robot.distance()/1000, robot.angle(), gyro_sensor.angle()/factor)


# data = DataLog('time / s', 'angle motors / °', 'distance ultrasonic / mm', 'distance infrared / %', name='surrounding', timestamp=False)
# robot.drive(speed = 0, turn_rate = 12)     # mm/s, deg/s
# for n in range(300):
#     data.log(watch.time()/1000, robot.angle(), distance_sensor.distance(), obstacle_sensor.distance() )
#     wait(100)
# robot.stop()


angle = 0

while True:
    robot.drive(speed = 100, turn_rate = 0)     # mm/s, deg/s

    while obstacle_sensor.distance() > 20 and bumper.pressed() is False:
        wait(100)    # ms

    robot.straight(-50)     # mm
    
    data.log(watch.time()/1000, robot.distance()/1000, angle, gyro_sensor.angle()/factor)

    robot.turn( random.randint(30,180) )  # °
    angle += robot.angle()

    robot.reset()