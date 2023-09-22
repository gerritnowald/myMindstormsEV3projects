#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, InfraredSensor, GyroSensor)
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

import random

#------------------------------------------------------------------------------
# initialization

obstacle_sensor = InfraredSensor(Port.S4)
bumper          = TouchSensor(Port.S3)
gyro_sensor     = GyroSensor(Port.S2)
gyro_sensor.reset_angle(0)

robot = DriveBase(left_motor = Motor(Port.B), right_motor = Motor(Port.C), wheel_diameter = 62.4, axle_track = 110)     # mm
robot.settings(straight_speed = 100, straight_acceleration = 100, turn_rate = 100, turn_acceleration = 100)

data  = DataLog('time / s', 'distance / mm', 'angle motors / °', 'angle gyro / °', name='path', timestamp=False)
data.log(0, 0, 0, 0)
watch = StopWatch()

#------------------------------------------------------------------------------
# calibration

robot.turn(360)  # °
factor = gyro_sensor.angle() / 360

robot.reset()
gyro_sensor.reset_angle(0)

#------------------------------------------------------------------------------
# main loop

angle = 0

while True:
    robot.drive(speed = 100, turn_rate = 0)     # mm/s, deg/s

    while obstacle_sensor.distance() > 20 and bumper.pressed() is False:
        wait(100)    # ms

    robot.straight(-50)     # mm
    
    data.log(watch.time()/1000, robot.distance()/1000, angle, gyro_sensor.angle()/factor)

    robot.turn( random.randint(30,180) * random.choice([1,-1]) )  # °
    angle += robot.angle()

    robot.reset()