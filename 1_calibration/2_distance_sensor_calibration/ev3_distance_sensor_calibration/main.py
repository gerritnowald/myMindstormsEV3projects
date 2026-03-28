#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, InfraredSensor, GyroSensor, UltrasonicSensor)
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

wheel_diameter =  62.4     # mm
axle_track     = 109.605   # mm

#------------------------------------------------------------------------------
# initialization

distance_sensor = UltrasonicSensor(Port.S1)
obstacle_sensor = InfraredSensor(Port.S4)

robot = DriveBase(left_motor = Motor(Port.B), right_motor = Motor(Port.C), wheel_diameter = wheel_diameter, axle_track = axle_track )
robot.settings(straight_speed = 100, straight_acceleration = 100, turn_rate = 100, turn_acceleration = 100)

watch = StopWatch()

#------------------------------------------------------------------------------
# calibration

data  = DataLog('time / s', 'distance driven motor / mm', 'distance ultrasonic / mm', 'distance infrared / %', name='distance_sensor', timestamp=False)
robot.drive(speed = 100, turn_rate = 0)
for n in range(300):    # 30 seconds at 100 mm/s = 3 m
    data.log(watch.time()/1000, robot.distance(), distance_sensor.distance(), obstacle_sensor.distance())
    wait(100)   # ms
robot.stop()