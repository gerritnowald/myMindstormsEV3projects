#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
# from pybricks.media.ev3dev import SoundFile, ImageFile

import random

#------------------------------------------------------------------------------
# initialization

ev3 = EV3Brick()

left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

obstacle_sensor = InfraredSensor(Port.S4)
bumper          = TouchSensor(Port.S3)

robot = DriveBase(left_motor, right_motor, wheel_diameter = 62.4, axle_track = 110)     # mm
robot.settings(straight_speed = 100, straight_acceleration = 100, turn_rate = 100, turn_acceleration = 100)

data  = DataLog('time / s', 'distance / mm', 'angle / °', name='path', timestamp=False)
watch = StopWatch()

#------------------------------------------------------------------------------
# main loop

while True:
    robot.drive(speed = 100, turn_rate = 0)     # mm/s, deg/s

    while obstacle_sensor.distance() > 20 and bumper.pressed() is False:
        wait(100)    # ms
    
    robot.straight(-50)     # mm

    data.log(watch.time()/1000, robot.distance(), robot.angle())    # old angle

    robot.turn(random.randint(30,180))  # °