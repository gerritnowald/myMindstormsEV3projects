#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, InfraredSensor, GyroSensor, UltrasonicSensor)
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

#------------------------------------------------------------------------------
# initialization

distance_sensor = UltrasonicSensor(Port.S1)
obstacle_sensor = InfraredSensor(Port.S4)

robot = DriveBase(left_motor = Motor(Port.B), right_motor = Motor(Port.C), wheel_diameter = 62.4, axle_track = 109.605 )     # mm
robot.settings(straight_speed = 100, straight_acceleration = 100, turn_rate = 100, turn_acceleration = 100)

watch = StopWatch()

#------------------------------------------------------------------------------
# calibration

# data  = DataLog('time / s', 'distance driven motor / mm', 'distance ultrasonic / mm', 'distance infrared / %', name='distance_sensor', timestamp=False)
# robot.drive(speed = 100, turn_rate = 0)
# for n in range(300):
#     data.log(watch.time()/1000, robot.distance(), distance_sensor.distance(), obstacle_sensor.distance())
#     wait(100)
# robot.stop()

#------------------------------------------------------------------------------
# turn

data = DataLog('time / s', 'angle motors / °', 'distance ultrasonic / mm', 'distance infrared / %', name='surrounding', timestamp=False)
robot.drive(speed = 0, turn_rate = 12)     # mm/s, deg/s
for n in range(300):
    data.log(watch.time()/1000, robot.angle(), distance_sensor.distance(), obstacle_sensor.distance() )
    wait(100)
robot.stop()