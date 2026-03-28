#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

wheel_diameter =  62.4     # mm
axle_track     = 109.605   # mm

#------------------------------------------------------------------------------
# initialization

robot = DriveBase(left_motor = Motor(Port.B), right_motor = Motor(Port.C), wheel_diameter = wheel_diameter, axle_track = axle_track )
robot.settings(straight_speed = 100, straight_acceleration = 100, turn_rate = 100, turn_acceleration = 100)

#------------------------------------------------------------------------------
# calibration wheel diameter
# - if the robot drives not far enough, decrease the wheel_diameter value.
# - if the robot drives too far,        increase the wheel_diameter value.

# robot.straight(1000)     # mm

#------------------------------------------------------------------------------
# calibration wheel distance
# - if the robot turns not far enough, increase the axle_track value.
# - if the robot turns too far,        decrease the axle_track value.

robot.turn(10*360)   # degree