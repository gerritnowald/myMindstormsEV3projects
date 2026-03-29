#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, InfraredSensor, GyroSensor)
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

import random

wheel_diameter =  62.4     # mm
axle_track     = 109.605   # mm

speed          = 100       # mm/s
turn_rate      = 60        # deg/s
angle_resolution = 10       # deg 

#------------------------------------------------------------------------------
# initialization

infrared_sensor = InfraredSensor(Port.S4)
gyro_sensor     = GyroSensor(Port.S2)
bumper          = TouchSensor(Port.S3)

robot = DriveBase(left_motor = Motor(Port.B), right_motor = Motor(Port.C), wheel_diameter = wheel_diameter, axle_track = axle_track )
robot.settings(straight_speed = speed, straight_acceleration = 100, turn_rate = turn_rate, turn_acceleration = 100)

data  = DataLog('time / s', 'distance / mm', 'angle motors / °', 'angle gyro / °', 'distance infrared / %', name='path', timestamp=False)

def log_data():
    data.log(watch.time()/1000, robot.distance(), robot.angle(), gyro_sensor.angle(), infrared_sensor.distance() )

watch = StopWatch()

#------------------------------------------------------------------------------
# calibration

Δt = angle_resolution / turn_rate

robot.reset()
gyro_sensor.reset_angle(0)

robot.drive(speed = 0, turn_rate = turn_rate)
for n in range(360/angle_resolution):
    wait(Δt * 1000)   # ms
    log_data()

#------------------------------------------------------------------------------
# main loop

while True:
    robot.drive(speed = speed, turn_rate = 0)

    while infrared_sensor.distance() > 30 and bumper.pressed() is False:
        wait(100)    # ms

    # stop and log data
    robot.straight(-50)     # mm
    log_data()

    # turn and log data
    robot.drive(speed = 0, turn_rate = turn_rate)
    for n in range(random.randint(30,180)/angle_resolution):
        wait(Δt * 1000)   # ms
        log_data()