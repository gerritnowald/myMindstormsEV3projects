#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
# from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
# from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()

# Initialize the motors.
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=62.4, axle_track=118)


robot.straight(1000)

robot.turn(180)

robot.straight(800)

robot.turn(180)

robot.straight(-200)