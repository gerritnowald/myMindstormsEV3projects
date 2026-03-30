#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.ev3devices import (Motor, GyroSensor)
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, DataLog

wheel_diameter =  62.4     # mm
axle_track     = 109.605   # mm

turn_rate        = 60      # deg/s
angle_resolution = 10      # deg 

#------------------------------------------------------------------------------
# initialization

robot = DriveBase(left_motor = Motor(Port.B), right_motor = Motor(Port.C), wheel_diameter = wheel_diameter, axle_track = axle_track )
robot.settings(straight_speed = 100, straight_acceleration = 100, turn_rate = turn_rate, turn_acceleration = 100)

gyro_sensor = GyroSensor(Port.S2)

watch = StopWatch()

data  = DataLog('time / s', 'angle motors / °', 'angle gyro / °', name='angles', timestamp=False)

def log_data():
    data.log(watch.time()/1000, robot.angle(), gyro_sensor.angle() )

#------------------------------------------------------------------------------
# calibration

Δt = angle_resolution / turn_rate

robot.reset()
gyro_sensor.reset_angle(0)

# turn
robot.drive(speed = 0, turn_rate = turn_rate)
for n in range(360/angle_resolution):
    wait(Δt * 1000)   # ms
    log_data()


# wait & measure
for n in range(60):
    wait(1000)    # ms
    log_data()